#!/usr/bin/env python3
"""
Convert resolved OGC Building Block schemas to JSON Forms-compatible Draft 7.

Reads from:  build/annotated/bbr/metadata/profiles/{profile}/schema.json
Writes to:   build/jsonforms/profiles/{profile}/schema.json

Conversion rules:
  1. $schema → Draft 7
  2. $defs → definitions, update internal $ref paths
  3. Strip $id, x-jsonld-* metadata keys
  4. Simplify anyOf patterns for form rendering
  5. const arrays → default values
  6. contains constraints → enum on items (technique profiles)
  7. allOf in technique profiles → merge base + constraints
  8. Inline all $ref references (fully resolved output)

Usage:
    python tools/convert_for_jsonforms.py --all
    python tools/convert_for_jsonforms.py --profile adaProduct
    python tools/convert_for_jsonforms.py --profile adaEMPA --verbose
"""

import argparse
import copy
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
ANNOTATED_DIR = REPO_ROOT / "build" / "annotated" / "bbr" / "metadata"
OUTPUT_DIR = REPO_ROOT / "build" / "jsonforms" / "profiles"
SOURCES_DIR = REPO_ROOT / "_sources" / "jsonforms" / "profiles"

ADA_PROFILES = ["adaProduct", "adaEMPA", "adaXRD", "adaICPMS", "adaVNMIR"]

# Keys to strip from schemas (metadata, not useful for forms)
STRIP_KEYS = {"$id", "x-jsonld-prefixes", "x-jsonld-context", "x-jsonld-extra-terms"}

# GitHub Pages URL prefix → local path mapping
GHPAGES_PREFIX = "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/"
LOCAL_ANNOTATED = REPO_ROOT / "build" / "annotated"


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

def _resolve_json_pointer(schema: dict, pointer: str) -> Any:
    """Resolve a JSON Pointer (e.g., '/$defs/empa_detail') within a schema."""
    parts = pointer.lstrip("/").split("/")
    current = schema
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list):
            current = current[int(part)]
        else:
            raise KeyError(f"Cannot resolve pointer /{'/'.join(parts)} at part '{part}'")
    return current


def resolve_external_refs(schema: Any) -> Any:
    """
    Resolve $ref URLs pointing to GitHub Pages into inline schemas
    by loading from the local build/annotated directory.
    Handles both plain file refs and refs with JSON Pointer fragments.
    """
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref = schema["$ref"]
            if isinstance(ref, str) and ref.startswith(GHPAGES_PREFIX):
                # Split URL from fragment
                if "#" in ref:
                    url_part, fragment = ref.split("#", 1)
                else:
                    url_part, fragment = ref, None

                # Map URL to local path
                relative = url_part[len(GHPAGES_PREFIX):]
                local_path = LOCAL_ANNOTATED / relative.replace("/", os.sep)

                if local_path.exists():
                    loaded = load_json(local_path)
                    # Resolve fragment pointer if present
                    if fragment:
                        try:
                            loaded = _resolve_json_pointer(loaded, fragment)
                        except KeyError as e:
                            print(f"WARNING: Could not resolve fragment {fragment} in {local_path}: {e}", file=sys.stderr)
                            return schema
                    # Recursively resolve any refs in the loaded schema
                    loaded = resolve_external_refs(loaded)
                    # Strip metadata from inlined schema
                    loaded = strip_metadata_keys(loaded)
                    return loaded
                else:
                    print(f"WARNING: Could not resolve $ref locally: {ref}", file=sys.stderr)
                    print(f"  Expected at: {local_path}", file=sys.stderr)
                    return schema

        result = {}
        for k, v in schema.items():
            result[k] = resolve_external_refs(v)
        return result
    elif isinstance(schema, list):
        return [resolve_external_refs(item) for item in schema]
    return schema


def strip_metadata_keys(schema: Any) -> Any:
    """Recursively remove metadata keys like $id, x-jsonld-*."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k in STRIP_KEYS:
                continue
            if k.startswith("x-jsonld"):
                continue
            result[k] = strip_metadata_keys(v)
        return result
    elif isinstance(schema, list):
        return [strip_metadata_keys(item) for item in schema]
    return schema


def convert_draft_version(schema: dict) -> dict:
    """Change $schema to Draft 7."""
    if "$schema" in schema:
        schema["$schema"] = "http://json-schema.org/draft-07/schema#"
    return schema


def convert_defs_to_definitions(schema: Any) -> Any:
    """Rename $defs → definitions and update all #/$defs/ refs to #/definitions/."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            new_key = "definitions" if k == "$defs" else k
            if k == "$ref" and isinstance(v, str):
                v = v.replace("#/$defs/", "#/definitions/")
            result[new_key] = convert_defs_to_definitions(v)
        return result
    elif isinstance(schema, list):
        return [convert_defs_to_definitions(item) for item in schema]
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
    →  {type: array, items: {type: string, enum: ["X"]}}

    {type: array, items: {type: string}, contains: {enum: [...]}}
    →  {type: array, items: {type: string, enum: [...]}}

    Also handles allOf with multiple contains.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            result[k] = simplify_contains_to_enum(v)

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


def simplify_anyof_identifier(prop_schema: dict) -> dict:
    """
    Simplify schema:identifier anyOf to a single string field for forms.
    The full anyOf with PropertyValue/array/string is too complex for form input.
    """
    return {
        "type": "string",
        "description": prop_schema.get("description", "Primary identifier for the dataset"),
    }


def simplify_anyof_license_items(items_schema: dict) -> dict:
    """
    Simplify schema:license items anyOf to CreativeWork object.
    """
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
    """
    Simplify schema:contributor items anyOf to Person with optional role.
    """
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
    """
    Simplify funder anyOf to inline Organization object.
    """
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
    """
    Simplify schema:creator @list items anyOf Person/Org to Person
    with a _creatorType selector.
    """
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
    """Simplify propertyID items anyOf to string or DefinedTerm."""
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


def simplify_file_detail_anyof(schema: dict) -> dict:
    """
    Simplify fileDetail anyOf (image/tabular/collection/etc) to a generic object.
    For forms, we don't need the full discriminated union.
    """
    return {
        "type": "object",
        "description": "Type-specific file details",
        "properties": {
            "@type": {
                "type": "array",
                "items": {"type": "string"},
                "description": "File detail type identifiers",
            },
        },
    }


def apply_anyof_simplifications(schema: Any, path: str = "") -> Any:
    """
    Walk the schema and apply anyOf simplifications at known locations.
    Uses the property path to identify which simplification to apply.
    """
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            current_path = f"{path}/{k}" if path else k

            # schema:identifier at top level → simplify
            if k == "schema:identifier" and path == "properties" and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_identifier(v)
                continue

            # schema:license items anyOf
            if k == "items" and path.endswith("schema:license") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_license_items(v)
                continue

            # schema:contributor items anyOf
            if k == "items" and path.endswith("schema:contributor") and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_anyof_contributor_items(v)
                continue

            # funder anyOf in funding items
            if k == "funder" and "schema:funding" in path and isinstance(v, dict) and "anyOf" in v:
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

            # fileDetail anyOf
            if k == "fileDetail" and isinstance(v, dict) and "anyOf" in v:
                result[k] = simplify_file_detail_anyof(v)
                continue

            # @type anyOf patterns (e.g., Organization types)
            if k == "@type" and isinstance(v, dict) and "anyOf" in v:
                # These are typically discriminated unions like [{"const": ["schema:Organization"]}]
                # Simplify to first const value as default
                first_anyof = v["anyOf"][0] if v["anyOf"] else {}
                if "const" in first_anyof:
                    result[k] = {
                        "type": "array" if isinstance(first_anyof["const"], list) else "string",
                        "default": first_anyof["const"],
                    }
                else:
                    result[k] = apply_anyof_simplifications(v, current_path)
                continue

            # distribution items oneOf → simplified
            if k == "items" and path.endswith("schema:distribution") and isinstance(v, dict) and "oneOf" in v:
                result[k] = simplify_distribution_items(v)
                continue

            result[k] = apply_anyof_simplifications(v, current_path)

        return result
    elif isinstance(schema, list):
        return [apply_anyof_simplifications(item, path) for item in schema]
    return schema


def simplify_distribution_items(items_schema: dict) -> dict:
    """
    Simplify distribution items oneOf (single file vs archive with hasPart)
    to a single object that covers both cases.
    """
    return {
        "type": "object",
        "description": "Data file or archive distribution",
        "properties": {
            "@type": {
                "type": "array",
                "items": {"type": "string"},
                "default": ["schema:DataDownload"],
            },
            "schema:name": {"type": "string"},
            "schema:description": {"type": "string"},
            "schema:contentURL": {
                "type": "string",
                "description": "Download URL for the file",
            },
            "schema:encodingFormat": {
                "type": "array",
                "items": {"type": "string"},
                "description": "MIME type(s)",
            },
            "schema:additionalType": {
                "type": "array",
                "items": {"type": "string"},
            },
            "spdx:checksum": {
                "type": "object",
                "properties": {
                    "spdx:algorithm": {"type": "string"},
                    "spdx:checksumValue": {"type": "string"},
                },
            },
            "schema:hasPart": {
                "type": "array",
                "description": "Files within an archive package",
                "items": {
                    "type": "object",
                    "properties": {
                        "@id": {"type": "string"},
                        "@type": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "schema:additionalType": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "schema:name": {"type": "string"},
                        "schema:description": {"type": "string"},
                        "schema:encodingFormat": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "schema:size": {
                            "type": "object",
                            "properties": {
                                "@type": {
                                    "type": "string",
                                    "default": "schema:QuantitativeValue",
                                },
                                "schema:value": {"type": "integer"},
                                "schema:unitText": {
                                    "type": "string",
                                    "default": "byte",
                                },
                            },
                        },
                        "spdx:checksum": {
                            "type": "object",
                            "properties": {
                                "spdx:algorithm": {"type": "string"},
                                "spdx:checksumValue": {"type": "string"},
                            },
                        },
                    },
                },
            },
        },
    }


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


def resolve_all_refs(schema: Any, definitions: dict) -> Any:
    """
    Inline all $ref references from definitions into the schema.
    This produces a fully resolved schema with no $ref.
    """
    if isinstance(schema, dict):
        if "$ref" in schema and len(schema) == 1:
            ref = schema["$ref"]
            if ref.startswith("#/definitions/"):
                def_name = ref[len("#/definitions/"):]
                if def_name in definitions:
                    resolved = copy.deepcopy(definitions[def_name])
                    return resolve_all_refs(resolved, definitions)
            elif ref.startswith("#/$defs/"):
                def_name = ref[len("#/$defs/"):]
                if def_name in definitions:
                    resolved = copy.deepcopy(definitions[def_name])
                    return resolve_all_refs(resolved, definitions)
            return schema

        result = {}
        for k, v in schema.items():
            if k in ("definitions", "$defs"):
                continue  # Don't recurse into definitions themselves
            result[k] = resolve_all_refs(v, definitions)
        return result
    elif isinstance(schema, list):
        return [resolve_all_refs(item, definitions) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# Technique profile merging
# ---------------------------------------------------------------------------

def merge_allof_entries(schema: dict) -> dict:
    """
    Flatten a schema that uses allOf to compose building blocks.
    Copies all top-level keys except allOf, then deep-merges each non-$ref
    allOf entry into the result. $ref entries are skipped because the OGC
    postprocessor resolves them into the built schema.json already.
    """
    merged = {}
    for k, v in schema.items():
        if k != "allOf":
            merged[k] = copy.deepcopy(v)
    for part in schema.get("allOf", []):
        if "$ref" in part:
            continue
        if isinstance(part, dict):
            merged = deep_merge(merged, part)
    return merged


def deep_merge(base: dict, overlay: dict) -> dict:
    """
    Deep merge overlay into base. overlay values take precedence.
    For arrays, overlay replaces base.
    For dicts, merge recursively.
    """
    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


def merge_technique_profile(profile_schema: dict, base_schema: dict) -> dict:
    """
    Merge a technique profile (allOf[$ref base, constraints]) into a single schema.
    The technique profile adds enum constraints on schema:additionalType and
    schema:hasPart/schema:additionalType.
    """
    if "allOf" not in profile_schema:
        return profile_schema

    # Collect all non-$ref parts from the allOf
    constraints = {}
    for part in profile_schema.get("allOf", []):
        if "$ref" in part:
            continue  # Skip the base $ref
        if isinstance(part, dict):
            constraints = deep_merge(constraints, part)

    # Start with a copy of the base schema
    merged = copy.deepcopy(base_schema)

    # Apply technique-specific property constraints
    if "properties" in constraints:
        for prop_name, constraint in constraints["properties"].items():
            if prop_name in merged.get("properties", {}):
                merged["properties"][prop_name] = deep_merge(
                    merged["properties"][prop_name], constraint
                )
            else:
                merged["properties"][prop_name] = constraint

    # Copy over title and description from the technique profile
    if "title" in profile_schema:
        merged["title"] = profile_schema["title"]
    if "description" in profile_schema:
        merged["description"] = profile_schema["description"]

    return merged


# ---------------------------------------------------------------------------
# Main conversion pipeline
# ---------------------------------------------------------------------------

def convert_profile_schema(
    profile_name: str,
    verbose: bool = False,
) -> dict:
    """
    Convert a single profile schema to JSON Forms-compatible Draft 7.

    For technique profiles (adaEMPA, etc.), this:
      1. Loads the base adaProduct schema
      2. Loads the technique profile
      3. Merges them
      4. Applies all simplifications

    For adaProduct, it just applies simplifications directly.
    """
    profile_dir = ANNOTATED_DIR / "profiles" / profile_name
    schema_path = profile_dir / "schema.json"

    if not schema_path.exists():
        print(f"ERROR: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Converting {profile_name}...", file=sys.stderr)

    schema = load_json(schema_path)

    # For adaProduct: flatten its own allOf (cdifMandatory + cdifOptional + ADA overrides)
    if profile_name == "adaProduct" and "allOf" in schema:
        schema = merge_allof_entries(schema)

    # For technique profiles, merge with base adaProduct
    if profile_name != "adaProduct" and "allOf" in schema:
        base_path = ANNOTATED_DIR / "profiles" / "adaProduct" / "schema.json"
        base_schema = load_json(base_path)
        # Flatten the base if it also uses allOf (e.g., from cdifMandatory/cdifOptional)
        if "allOf" in base_schema:
            base_schema = merge_allof_entries(base_schema)
        schema = merge_technique_profile(schema, base_schema)

    # Pipeline: apply all transformations in order
    schema = resolve_external_refs(schema)
    schema = strip_metadata_keys(schema)
    schema = convert_draft_version(schema)

    # Resolve definitions inline before simplification
    definitions = schema.get("$defs", schema.get("definitions", {}))
    if definitions:
        schema = resolve_all_refs(schema, definitions)
        schema.pop("$defs", None)
        schema.pop("definitions", None)

    schema = apply_anyof_simplifications(schema, "")
    schema = simplify_const_to_default(schema)
    schema = simplify_contains_to_enum(schema)
    schema = remove_not_constraints(schema)

    # Final cleanup: remove minItems constraints that are too restrictive for forms
    schema = relax_min_items(schema)

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


def main():
    parser = argparse.ArgumentParser(
        description="Convert BB schemas to JSON Forms Draft 7 format",
    )
    parser.add_argument(
        "--profile",
        help="Convert a single profile (e.g., adaProduct)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Convert all ADA profiles",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print progress information",
    )
    args = parser.parse_args()

    if not args.all and not args.profile:
        parser.error("Specify --all or --profile <name>")

    profiles = ADA_PROFILES if args.all else [args.profile]

    for profile in profiles:
        schema = convert_profile_schema(profile, args.verbose)
        output_path = OUTPUT_DIR / profile / "schema.json"
        save_json(schema, output_path)
        if args.verbose:
            print(f"  → {output_path}", file=sys.stderr)

        # Copy uischema.json and defaults.json from _sources/ to build/
        for static_file in ("uischema.json", "defaults.json"):
            src = SOURCES_DIR / profile / static_file
            dst = OUTPUT_DIR / profile / static_file
            if src.exists():
                shutil.copy2(str(src), str(dst))
                if args.verbose:
                    print(f"  → {dst} (copied from _sources)", file=sys.stderr)
            elif args.verbose:
                print(f"  WARNING: {src} not found", file=sys.stderr)

    print(f"Converted {len(profiles)} profile(s) to {OUTPUT_DIR}", file=sys.stderr)


if __name__ == "__main__":
    main()
