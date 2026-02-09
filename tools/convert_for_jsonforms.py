#!/usr/bin/env python3
"""
Convert resolved OGC Building Block schemas to JSON Forms-compatible Draft 7.

Reads from:  _sources/profiles/{profile}/resolvedSchema.json  (resolve_schema.py output)
Writes to:   build/jsonforms/profiles/{profile}/schema.json

Conversion rules:
  1. Strip $id, x-jsonld-* metadata keys
  2. $schema → Draft 7
  3. Simplify anyOf patterns for form rendering
  4. const arrays → default values
  5. contains constraints → enum on items
  6. Remove 'not' constraints
  7. Flatten leftover allOf entries
  8. Remove minItems constraints

The input schemas are already fully resolved (no $ref, no $defs).

Usage:
    python tools/convert_for_jsonforms.py --all
    python tools/convert_for_jsonforms.py --profile adaProduct
    python tools/convert_for_jsonforms.py --profile adaEMPA --verbose
"""

import argparse
import copy
import json
import shutil
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
RESOLVED_DIR = REPO_ROOT / "_sources" / "profiles"
OUTPUT_DIR = REPO_ROOT / "build" / "jsonforms" / "profiles"
SOURCES_DIR = REPO_ROOT / "_sources" / "jsonforms" / "profiles"

ADA_PROFILES = ["adaProduct", "adaEMPA", "adaXRD", "adaICPMS", "adaVNMIR"]
CDIF_PROFILES = ["CDIFDiscovery"]
ALL_PROFILES = ADA_PROFILES + CDIF_PROFILES

# Keys to strip from schemas (metadata, not useful for forms)
STRIP_KEYS = {"$id", "x-jsonld-prefixes", "x-jsonld-context", "x-jsonld-extra-terms"}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------------------
# Core conversion helpers
# ---------------------------------------------------------------------------

def strip_metadata_keys(schema: Any, is_root: bool = True) -> Any:
    """Recursively remove metadata keys like $id, x-jsonld-*. Also strip $schema from nested objects."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k in STRIP_KEYS:
                continue
            if k.startswith("x-jsonld"):
                continue
            # Strip $schema from nested objects (keep only at root)
            if k == "$schema" and not is_root:
                continue
            result[k] = strip_metadata_keys(v, is_root=False)
        return result
    elif isinstance(schema, list):
        return [strip_metadata_keys(item, is_root=False) for item in schema]
    return schema


def convert_draft_version(schema: dict) -> dict:
    """Change $schema to Draft 7."""
    if "$schema" in schema:
        schema["$schema"] = "http://json-schema.org/draft-07/schema#"
    return schema


def simplify_const_to_default(schema: Any) -> Any:
    """
    Convert const values to default values for form pre-population.
    const arrays like {"const": ["schema:Dataset", "schema:Product"]} become
    {"default": ["schema:Dataset", "schema:Product"]}.
    const strings remain as default strings.
    Also handles the pattern where const is used alongside type.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            result[k] = simplify_const_to_default(v)

        # If const is present, convert to default and remove const
        if "const" in result:
            const_val = result.pop("const")
            if "default" not in result:
                result["default"] = const_val
            # Add type if not present
            if "type" not in result:
                if isinstance(const_val, list):
                    result["type"] = "array"
                elif isinstance(const_val, str):
                    result["type"] = "string"

        return result
    elif isinstance(schema, list):
        return [simplify_const_to_default(item) for item in schema]
    return schema


def simplify_contains_to_enum(schema: Any) -> Any:
    """
    Convert contains constraints to enum on items.
    {type: array, items: {type: string}, contains: {const: "X"}}
    ->  {type: array, items: {type: string, enum: ["X"]}}

    {type: array, items: {type: string}, contains: {enum: [...]}}
    ->  {type: array, items: {type: string, enum: [...]}}

    Also handles allOf with multiple contains.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            result[k] = simplify_contains_to_enum(v)

        # Strip contains from non-array types (invalid placement)
        if "contains" in result and result.get("type") != "array":
            result.pop("contains")

        if "contains" in result and result.get("type") == "array":
            contains = result.pop("contains")
            if "const" in contains:
                enum_vals = [contains["const"]]
            elif "enum" in contains:
                enum_vals = contains["enum"]
            else:
                enum_vals = None

            if enum_vals is not None:
                if "items" not in result:
                    result["items"] = {"type": "string"}
                if isinstance(result["items"], dict):
                    result["items"]["enum"] = enum_vals

        # Handle allOf with contains patterns (e.g., @type requiring multiple values)
        if "allOf" in result and result.get("type") == "array":
            new_allof = []
            collected_enums = []
            for item in result["allOf"]:
                if isinstance(item, dict) and "contains" in item:
                    contains = item["contains"]
                    if "const" in contains:
                        collected_enums.append(contains["const"])
                    elif "enum" in contains:
                        collected_enums.extend(contains["enum"])
                else:
                    new_allof.append(item)

            if collected_enums:
                # Set as default values for the array
                if "default" not in result:
                    result["default"] = collected_enums
                if "items" not in result:
                    result["items"] = {"type": "string"}

            if new_allof:
                result["allOf"] = new_allof
            else:
                result.pop("allOf", None)

        return result
    elif isinstance(schema, list):
        return [simplify_contains_to_enum(item) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# anyOf simplification helpers
# ---------------------------------------------------------------------------

def simplify_anyof_license_items(items_schema: dict) -> dict:
    """Simplify schema:license items anyOf to CreativeWork object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:CreativeWork",
            },
            "schema:name": {"type": "string"},
            "schema:description": {"type": "string"},
            "schema:url": {"type": "string"},
        },
    }


def simplify_anyof_contributor_items(items_schema: dict) -> dict:
    """Simplify schema:contributor items anyOf to Person with optional role."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "ORCID or other identifier",
            },
            "schema:affiliation": {
                "type": "object",
                "properties": {
                    "schema:name": {"type": "string"},
                },
            },
            "schema:roleName": {
                "type": "string",
                "description": "Role of the contributor",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_funder(funder_schema: dict) -> dict:
    """Simplify funder anyOf to inline Organization object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_creator_items(items_schema: dict) -> dict:
    """Simplify schema:creator @list items anyOf Person/Org to Person with selector."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
            "schema:alternateName": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "ORCID or other identifier",
            },
            "schema:affiliation": {
                "type": "object",
                "properties": {
                    "schema:name": {"type": "string"},
                },
            },
            "schema:description": {"type": "string"},
        },
        "required": ["@type", "schema:name"],
    }


def simplify_anyof_maintainer(schema: dict) -> dict:
    """Simplify schema:maintainer anyOf to Person object."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Person",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_provider_items(schema: dict) -> dict:
    """Simplify distribution provider items anyOf to Organization."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_measurement_technique(schema: dict) -> dict:
    """Simplify variableMeasured measurementTechnique anyOf."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
        },
        "required": ["schema:name"],
    }


def simplify_anyof_unit_code(schema: dict) -> dict:
    """Simplify unitCode anyOf to string."""
    return {"type": "string"}


def simplify_anyof_property_id_items(schema: dict) -> dict:
    """Simplify propertyID items anyOf to DefinedTerm."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {"type": "string"},
            "schema:inDefinedTermSet": {"type": "string"},
            "schema:termCode": {"type": "string"},
        },
    }


def simplify_anyof_cdi_uses_items(schema: dict) -> dict:
    """Simplify cdi:uses items anyOf to DefinedTerm."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DefinedTerm",
            },
            "schema:name": {"type": "string"},
        },
    }


def simplify_anyof_conditions_of_access_items(schema: dict) -> dict:
    """Simplify schema:conditionsOfAccess items anyOf to LabeledLink (CreativeWork)."""
    return {
        "type": "object",
        "description": "Access condition — provide a label and optional URL",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:CreativeWork",
            },
            "schema:name": {
                "type": "string",
                "description": "Short label for the access condition",
            },
            "schema:description": {
                "type": "string",
                "description": "Detailed description of the condition",
            },
            "schema:url": {
                "type": "string",
                "format": "uri",
                "description": "URL to a document describing the access condition",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_publisher(schema: dict) -> dict:
    """Simplify schema:publisher anyOf to Organization."""
    return {
        "type": "object",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Organization",
                "enum": ["schema:Person", "schema:Organization"],
            },
            "schema:name": {"type": "string"},
            "schema:identifier": {
                "type": "string",
                "description": "Identifier (e.g. ROR, ORCID)",
            },
        },
        "required": ["schema:name"],
    }


def simplify_anyof_spatial_coverage_items(schema: dict) -> dict:
    """Simplify schema:spatialCoverage items to a place object."""
    return {
        "type": "object",
        "description": "Spatial extent of the dataset",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:Place",
            },
            "schema:name": {
                "type": "string",
                "description": "Place name",
            },
            "schema:geo": {
                "type": "object",
                "properties": {
                    "@type": {
                        "type": "string",
                        "default": "schema:GeoShape",
                    },
                    "schema:box": {
                        "type": "string",
                        "description": "Bounding box as 'south west north east'",
                    },
                },
            },
        },
    }


def simplify_anyof_temporal_coverage_items(schema: dict) -> dict:
    """Replace temporalCoverage items anyOf with a simple string."""
    return {
        "type": "string",
        "description": "ISO 8601 date, date range (e.g. 2020-01/2020-12), or text description",
    }


def simplify_anyof_keywords_items(schema: dict) -> dict:
    """Simplify schema:keywords items anyOf to string."""
    return {"type": "string"}


def simplify_anyof_publishing_principles_items(schema: dict) -> dict:
    """Simplify schema:publishingPrinciples items anyOf to string."""
    return {"type": "string", "description": "Publishing principle statement or URL"}


def simplify_anyof_additional_type_items(schema: dict) -> dict:
    """Simplify schema:additionalType items anyOf to string."""
    return {"type": "string", "description": "Additional type URI or label"}


def simplify_anyof_distribution_items_cdif(schema: dict) -> dict:
    """
    Replace CDIF distribution items anyOf with a single flat object containing
    all fields from DataDownload and WebAPI. The @type field indicates which type.
    """
    return {
        "type": "object",
        "description": "Distribution — Data Download or Web API",
        "properties": {
            "@type": {
                "type": "string",
                "default": "schema:DataDownload",
                "description": "schema:DataDownload for files, schema:WebAPI for APIs",
            },
            "schema:name": {"type": "string", "description": "Name of this distribution"},
            "schema:description": {"type": "string"},
            "schema:contentUrl": {
                "type": "string",
                "format": "uri",
                "description": "Download URL for the file (DataDownload)",
            },
            "schema:encodingFormat": {
                "type": "array",
                "items": {"type": "string"},
                "description": "MIME type(s) (DataDownload)",
            },
            "spdx:checksum": {
                "type": "object",
                "properties": {
                    "spdx:algorithm": {"type": "string"},
                    "spdx:checksumValue": {"type": "string"},
                },
            },
            "schema:serviceType": {
                "type": "string",
                "description": "Type of service, e.g. OGC:WMS, OPeNDAP (WebAPI)",
            },
            "schema:documentation": {
                "type": "string",
                "format": "uri",
                "description": "URL to API documentation (WebAPI)",
            },
        },
    }


def simplify_anyof_same_as_items(schema: dict) -> dict:
    """Simplify schema:sameAs items anyOf to string."""
    return {"type": "string", "description": "Alternate identifier or URL"}


# ---------------------------------------------------------------------------
# Distribution simplification — preserve oneOf structure
# ---------------------------------------------------------------------------

def simplify_distribution_items(items_schema: dict) -> dict:
    """
    Simplify distribution items while preserving the oneOf structure.
    Each oneOf branch (single file, archive, WebAPI) is kept as a distinct
    option so the form can render a distribution type selector.  Form-specific
    simplifications (const->default, contains->enum, etc.) are applied within
    each branch by the main pipeline — we just preserve the structure here.

    For technique profiles the resolved schema may have a top-level
    ``properties`` alongside ``oneOf`` (technique constraints that apply to all
    branches).  These are merged into each applicable oneOf branch.
    """
    result = copy.deepcopy(items_schema)

    # If technique-specific constraints sit alongside oneOf, merge them in
    if "oneOf" in result and "properties" in result:
        extra_props = result.pop("properties")
        for branch in result["oneOf"]:
            if isinstance(branch, dict) and "properties" in branch:
                for pk, pv in extra_props.items():
                    # Only merge into branches that have the relevant sub-property
                    # e.g. schema:hasPart only goes into the archive branch
                    if pk == "schema:hasPart" and pk in branch["properties"]:
                        branch["properties"][pk] = _deep_merge_dict(
                            branch["properties"][pk], pv
                        )
                    elif pk not in branch["properties"]:
                        # New property — add to all branches
                        branch["properties"][pk] = copy.deepcopy(pv)

    return result


def _deep_merge_dict(base: dict, overlay: dict) -> dict:
    """Simple recursive dict merge (overlay wins on conflicts)."""
    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge_dict(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


# ---------------------------------------------------------------------------
# fileDetail simplification — preserve anyOf structure
# ---------------------------------------------------------------------------

def simplify_file_detail_anyof(schema: dict) -> dict:
    """
    Preserve the fileDetail anyOf of file types.  Each file type keeps its
    @type, componentType (with enums), and type-specific detail properties.
    The form can use fileDetail.@type as a discriminator to show the right fields.

    We strip internal complexity (nested anyOf in componentType detail refs)
    but keep the overall structure.
    """
    if "anyOf" not in schema:
        return schema

    result = copy.deepcopy(schema)
    simplified = []
    for option in result["anyOf"]:
        if isinstance(option, dict):
            simplified.append(_simplify_file_type_option(option))
        else:
            simplified.append(option)
    result["anyOf"] = simplified
    return result


def _simplify_file_type_option(option: dict) -> dict:
    """
    Simplify a single file type option within fileDetail anyOf.
    Keeps @type, componentType (with enums + detail type refs), and
    type-specific properties.  Strips overly nested structures.
    """
    result = copy.deepcopy(option)

    # Simplify componentType if present — it may have nested anyOf for detail types
    props = result.get("properties", {})
    if "componentType" in props:
        ct = props["componentType"]
        if "anyOf" in ct:
            # componentType has anyOf of {enum + optional detail ref}
            # Keep the structure — each option has @type enum + detail properties
            pass  # Already structured, let it through

    return result


# ---------------------------------------------------------------------------
# Main anyOf simplification walker
# ---------------------------------------------------------------------------

def apply_anyof_simplifications(schema: Any, path: str = "") -> Any:
    """
    Walk the schema and apply anyOf simplifications at known locations.
    Uses the property path to identify which simplification to apply.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            current_path = f"{path}/{k}" if path else k

            # schema:identifier anyOf -> simplify (anywhere in schema)
            if k == "schema:identifier" and isinstance(v, dict) and "anyOf" in v:
                desc = v.get("description", "Identifier")
                result[k] = {"type": "string", "description": desc}
                continue

            # schema:license items anyOf
            if k == "items" and path.endswith("schema:license") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_license_items(v)
                continue

            # schema:contributor items anyOf
            if k == "items" and path.endswith("schema:contributor") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_contributor_items(v)
                continue

            # funder anyOf (in funding items or schema:funder)
            if k in ("funder", "schema:funder") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_funder(v)
                continue

            # schema:creator @list items anyOf
            if k == "items" and path.endswith("@list") and "schema:creator" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_creator_items(v)
                continue

            # schema:maintainer anyOf in subjectOf
            if k == "schema:maintainer" and "schema:subjectOf" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_maintainer(v)
                continue

            # schema:provider items anyOf in distribution
            if k == "items" and path.endswith("schema:provider") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_provider_items(v)
                continue

            # variableMeasured schema:measurementTechnique anyOf
            if k == "schema:measurementTechnique" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_measurement_technique(v)
                continue

            # variableMeasured schema:unitCode anyOf
            if k == "schema:unitCode" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_unit_code(v)
                continue

            # variableMeasured schema:propertyID items anyOf
            if k == "items" and path.endswith("schema:propertyID") and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_property_id_items(v)
                continue

            # variableMeasured cdi:uses items anyOf
            if k == "items" and path.endswith("cdi:uses") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_cdi_uses_items(v)
                continue

            # variableMeasured schema:identifier anyOf (nested in variable)
            if k == "schema:identifier" and "schema:variableMeasured" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string", "description": "Variable identifier"}
                continue

            # fileDetail anyOf — preserve structure with per-file-type simplification
            if k == "fileDetail" and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_file_detail_anyof(v)
                continue

            # @type anyOf patterns (e.g., Organization types)
            if k == "@type" and isinstance(v, dict) and "anyOf" in v:
                first_anyof = v["anyOf"][0] if v["anyOf"] else {}
                if "const" in first_anyof:
                    result[k] = {
                        "type": "array" if isinstance(first_anyof["const"], list) else "string",
                        "default": first_anyof["const"],
                    }
                else:
                    result[k] = apply_anyof_simplifications(v, current_path)
                continue

            # distribution items oneOf -> preserve structure (ADA)
            # After structural simplification, continue recursion into branches
            if k == "items" and path.endswith("schema:distribution") and isinstance(v, dict) and "oneOf" in v:
                simplified = simplify_distribution_items(v)
                result[k] = apply_anyof_simplifications(simplified, current_path)
                continue

            # distribution items anyOf -> simplified (CDIF: DataDownload/WebAPI)
            if k == "items" and path.endswith("schema:distribution") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_distribution_items_cdif(v)
                continue

            # schema:conditionsOfAccess items anyOf
            if k == "items" and path.endswith("schema:conditionsOfAccess") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_conditions_of_access_items(v)
                continue

            # schema:publisher anyOf (not an array, direct anyOf)
            if k == "schema:publisher" and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_publisher(v)
                continue

            # schema:spatialCoverage items
            if k == "items" and path.endswith("schema:spatialCoverage") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_spatial_coverage_items(v)
                continue

            # schema:temporalCoverage items
            if k == "items" and path.endswith("schema:temporalCoverage") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_temporal_coverage_items(v)
                continue

            # schema:keywords items anyOf
            if k == "items" and path.endswith("schema:keywords") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_keywords_items(v)
                continue

            # schema:publishingPrinciples items anyOf
            if k == "items" and path.endswith("schema:publishingPrinciples") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_publishing_principles_items(v)
                continue

            # schema:additionalType items anyOf
            if k == "items" and path.endswith("schema:additionalType") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_additional_type_items(v)
                continue

            # schema:sameAs items anyOf
            if k == "items" and path.endswith("schema:sameAs") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_same_as_items(v)
                continue

            # schema:geo anyOf (GeoShape vs GeoCoordinates) -> simplify to GeoShape
            if k == "schema:geo" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {
                    "type": "object",
                    "description": v.get("description", "Geographic extent"),
                    "properties": {
                        "@type": {"type": "string", "default": "schema:GeoShape"},
                        "schema:box": {
                            "type": "string",
                            "description": "Bounding box as 'south west north east'",
                        },
                    },
                }
                continue

            # schema:linkRelationship anyOf (DefinedTerm or string) -> simplify to string
            if k == "schema:linkRelationship" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string", "description": "How the linked resource is related"}
                continue

            # schema:name items anyOf in spatialCoverage (place names: DefinedTerm or string)
            if k == "items" and path.endswith("schema:name") and "schema:spatialCoverage" in path and isinstance(v, dict) and "anyOf" in v:
                result[k] = {"type": "string"}
                continue

            # schema:serviceType anyOf (string or DefinedTerm) -> simplify to string
            if k == "schema:serviceType" and isinstance(v, dict) and "anyOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "Type of service"),
                }
                continue

            # schema:documentation oneOf (string or LabeledLink) -> simplify to string
            if k == "schema:documentation" and isinstance(v, dict) and "oneOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "URL to API documentation"),
                }
                continue

            # schema:termsOfService oneOf (string or LabeledLink) -> simplify to string
            if k == "schema:termsOfService" and isinstance(v, dict) and "oneOf" in v:
                result[k] = {
                    "type": "string",
                    "description": v.get("description", "Terms of service"),
                }
                continue

            result[k] = apply_anyof_simplifications(v, current_path)

        return result
    elif isinstance(schema, list):
        return [apply_anyof_simplifications(item, path) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# Remaining cleanup passes
# ---------------------------------------------------------------------------

def remove_not_constraints(schema: Any) -> Any:
    """Remove 'not' constraints (e.g., not contains) that confuse form renderers."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k == "not":
                continue
            result[k] = remove_not_constraints(v)
        return result
    elif isinstance(schema, list):
        return [remove_not_constraints(item) for item in schema]
    return schema


def flatten_remaining_allof(schema: Any) -> Any:
    """
    Flatten leftover allOf entries that remain after merging.
    - Simple entries with only 'required' are merged into the parent.
    - Entries with 'anyOf' containing conditional-required rules are dropped
      (JSON Forms doesn't support conditional required).
    Applied recursively so it catches allOf inside items, properties, etc.
    """
    if isinstance(schema, dict):
        # Recurse first so nested allOf in properties/items are handled
        result = {}
        for k, v in schema.items():
            result[k] = flatten_remaining_allof(v)

        # Now flatten allOf in the current object
        if "allOf" in result:
            all_of = result["allOf"]
            keep = []
            for entry in all_of:
                if not isinstance(entry, dict):
                    keep.append(entry)
                    continue
                keys = set(entry.keys())
                if not keys:
                    # Empty entry — drop
                    continue
                if keys == {"required"}:
                    # Merge required into parent
                    existing = result.get("required", [])
                    merged = list(existing) + [
                        r for r in entry["required"] if r not in existing
                    ]
                    result["required"] = merged
                elif keys == {"anyOf"}:
                    # Conditional required — drop for form friendliness
                    continue
                else:
                    keep.append(entry)
            if not keep:
                del result["allOf"]
            else:
                result["allOf"] = keep
        return result
    elif isinstance(schema, list):
        return [flatten_remaining_allof(item) for item in schema]
    return schema


def relax_min_items(schema: Any) -> Any:
    """Remove or relax minItems constraints that prevent empty arrays in forms."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k == "minItems":
                continue  # Remove minItems from all arrays for form friendliness
            result[k] = relax_min_items(v)
        return result
    elif isinstance(schema, list):
        return [relax_min_items(item) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# Main conversion pipeline
# ---------------------------------------------------------------------------

def convert_profile_schema(
    profile_name: str,
    verbose: bool = False,
) -> dict:
    """
    Convert a single profile's resolvedSchema.json to JSON Forms Draft 7.

    Input:  _sources/profiles/{profile}/resolvedSchema.json
    Output: Fully simplified schema with no $ref, no $defs, Draft 7 compatible.
    """
    schema_path = RESOLVED_DIR / profile_name / "resolvedSchema.json"

    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Converting {profile_name} from {schema_path}...", file=sys.stderr)

    schema = load_json(schema_path)

    # Pipeline: apply all transformations in order.
    # Note: simplify_contains_to_enum must run BEFORE simplify_const_to_default,
    # because const_to_default converts {const: X} -> {default: X}, which would
    # prevent contains_to_enum from extracting the value.
    schema = strip_metadata_keys(schema)
    schema = convert_draft_version(schema)
    schema = apply_anyof_simplifications(schema, "")
    schema = simplify_contains_to_enum(schema)
    schema = simplify_const_to_default(schema)
    schema = remove_not_constraints(schema)
    schema = flatten_remaining_allof(schema)
    schema = relax_min_items(schema)

    # Strip enum from top-level @type items — the pick list values are provided
    # via uischema suggestion option to avoid JSON Forms scope resolution issues
    if "properties" in schema and "@type" in schema["properties"]:
        at_type = schema["properties"]["@type"]
        if "items" in at_type and isinstance(at_type["items"], dict):
            at_type["items"].pop("enum", None)

    return schema


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Convert resolved schemas to JSON Forms Draft 7 format",
    )
    parser.add_argument(
        "--profile",
        help="Convert a single profile (e.g., adaProduct)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Convert all profiles (ADA + CDIF)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print progress information",
    )
    args = parser.parse_args()

    if not args.all and not args.profile:
        parser.error("Specify --all or --profile <name>")

    profiles = ALL_PROFILES if args.all else [args.profile]

    for profile in profiles:
        schema = convert_profile_schema(profile, args.verbose)
        output_path = OUTPUT_DIR / profile / "schema.json"
        save_json(schema, output_path)
        if args.verbose:
            print(f"  -> {output_path}", file=sys.stderr)

        # Copy uischema.json and defaults.json from _sources/ to build/
        for static_file in ("uischema.json", "defaults.json"):
            src = SOURCES_DIR / profile / static_file
            dst = OUTPUT_DIR / profile / static_file
            if src.exists():
                shutil.copy2(str(src), str(dst))
                if args.verbose:
                    print(f"  -> {dst} (copied from _sources)", file=sys.stderr)
            elif args.verbose:
                print(f"  WARNING: {src} not found", file=sys.stderr)

    print(f"Converted {len(profiles)} profile(s) to {OUTPUT_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
