#!/usr/bin/env python3
"""Generate example JSON-LD instance documents for ADA profile building blocks.

Creates example{ProfileName}.json files that populate all keys defined by
each profile's schema with realistic mock data.

Usage:
    python tools/generate_examples.py            # generate all missing examples
    python tools/generate_examples.py adaSEM     # generate one profile
    python tools/generate_examples.py --all      # regenerate all (overwrite existing)
    python tools/generate_examples.py --list     # list profiles needing examples
"""

import argparse
import copy
import json
import sys
from pathlib import Path

# Import PROFILES from generate_profiles for the 31 generated profiles
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_profiles import PROFILES as GENERATED_PROFILES

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"
PROFILES_DIR = SOURCES_DIR / "profiles"

# ---------------------------------------------------------------------------
# Hand-crafted profile configs (not in generate_profiles.py PROFILES dict)
# ---------------------------------------------------------------------------

HANDCRAFTED_PROFILES = {
    "adaProduct": {
        "short_name": "ADA",
        "full_name": "Astromat Data Archive (ADA)",
        "description": "Base product metadata for the Astromat Data Archive.",
        "product_types": ["EMPAImage"],
        "additional_type_labels": [
            "Electron Microprobe Analysis Image (EMPA)",
        ],
        "component_types": ["EMPAImage", "EMPAImageMap"],
    },
    "adaEMPA": {
        "short_name": "EMPA",
        "full_name": "Electron Microprobe Analysis (EMPA)",
        "description": "Electron microprobe analysis imaging and quantitative elemental data.",
        "product_types": ["EMPAImage", "EMPACollection", "EMPAQEA", "EMPAESPC"],
        "additional_type_labels": [
            "Electron Microprobe Analysis Image (EMPA)",
        ],
        "component_types": [
            "EMPAImageMap", "EMPAImage", "EMPAQEATabular", "EMPAImageCollection",
        ],
    },
    "adaICPMS": {
        "short_name": "ICPMS",
        "full_name": "Inductively Coupled Plasma Mass Spectrometry (ICP-MS)",
        "description": "ICP-MS elemental and isotopic analysis data.",
        "product_types": [
            "HRICPMSProcessed", "HRICPMSRaw",
            "QICPMSProcessed", "QICPMSRaw",
            "MCICPMSRaw", "MCICPMSProcessed",
        ],
        "additional_type_labels": [
            "High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed",
        ],
        "component_types": [
            "HRICPMSProcessed", "HRICPMSRaw",
            "QICPMSProcessedTabular", "QICPMSRawTabular",
            "MCICPMSTabular",
        ],
    },
    "adaXRD": {
        "short_name": "XRD",
        "full_name": "X-ray Diffraction (XRD)",
        "description": "X-ray diffraction pattern and phase analysis data.",
        "product_types": ["XRDTabular"],
        "additional_type_labels": [
            "X-ray Diffraction (XRD) Tabular",
        ],
        "component_types": [
            "XRDTabular", "XRDDiffractionPattern", "XRDIndexedImage",
        ],
    },
    "adaVNMIR": {
        "short_name": "VNMIR",
        "full_name": "Visible, Near-Infrared, and Mid-Infrared Spectroscopy (VNMIR)",
        "description": "VNMIR reflectance spectroscopy point measurements.",
        "product_types": ["VNMIRPoint"],
        "additional_type_labels": [
            "Visible, near-infrared, and mid-infrared Spectroscopy (VNMIR) Point",
        ],
        "component_types": ["VNMIRPoint"],
    },
}


def get_all_ada_profiles() -> dict:
    """Merge hand-crafted and generated profile configs."""
    all_profiles = dict(HANDCRAFTED_PROFILES)
    all_profiles.update(GENERATED_PROFILES)
    return all_profiles


# ---------------------------------------------------------------------------
# Example JSON-LD template builder
# ---------------------------------------------------------------------------

def _get_additional_type(profile_name: str, cfg: dict) -> list:
    """Build the schema:additionalType array for an example.

    adaProduct uses human-readable labels from its enum;
    technique profiles use ada:-prefixed product types from their contains enum.
    """
    first_pt = cfg["product_types"][0]
    if profile_name == "adaProduct":
        # adaProduct's resolved schema has items.enum with human-readable labels
        label = cfg["additional_type_labels"][0] if cfg.get("additional_type_labels") else first_pt
        return [label, "ada:DataDeliveryPackage"]
    # Technique profiles have contains enum with ada: prefixed types
    return [f"ada:{first_pt}", "ada:DataDeliveryPackage"]


def build_example(profile_name: str, cfg: dict) -> dict:
    """Build a complete example JSON-LD instance for an ADA profile."""
    short = cfg["short_name"]
    full = cfg["full_name"]
    first_pt = cfg["product_types"][0]
    first_ct = cfg["component_types"][0] if cfg["component_types"] else first_pt

    # Pick a second component type for hasPart variety if available
    supporting_ct = "methodDescription"

    example = {
        "@context": {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
            "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
            "csvw": "http://www.w3.org/ns/csvw#",
            "prov": "http://www.w3.org/ns/prov#",
            "spdx": "http://spdx.org/rdf/terms#",
            "nxs": "http://purl.org/nexusformat/definitions/",
            "dcterms": "http://purl.org/dc/terms/",
            "geosparql": "http://www.opengis.net/ont/geosparql#",
            "ex": "https://example.org/",
        },
        "@id": f"ex:{profile_name}-example-001",
        "@type": ["schema:Dataset", "schema:Product"],
        "schema:name": f"{short} Analysis of Meteorite ALH 84001 Fragment",
        "schema:description": (
            f"Example {full} product metadata demonstrating all properties "
            f"defined by the {profile_name} profile. Contains mock data for "
            f"testing and validation."
        ),
        "schema:additionalType": _get_additional_type(profile_name, cfg),
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://registry.identifiers.org/registry/doi",
            "schema:value": f"10.99999/{profile_name.lower()}-example-001",
            "schema:url": f"https://doi.org/10.99999/{profile_name.lower()}-example-001",
        },
        "schema:url": f"https://astromat.org/products/{profile_name.lower()}-example-001",
        "schema:dateModified": "2026-01-15",
        "schema:version": "1.0",
        "schema:conditionsOfAccess": [
            "Unrestricted access for research purposes",
        ],
        "schema:license": [
            "https://creativecommons.org/licenses/by/4.0/",
        ],
        "schema:creativeWorkStatus": "Published",
        "schema:keywords": [
            {
                "@type": "schema:DefinedTerm",
                "schema:name": short,
                "schema:termCode": cfg.get("termcodes", [short])[0] if "termcodes" in cfg else short,
                "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques",
            },
            "meteorite",
            "astromaterials",
        ],
        "schema:creator": {
            "@list": [
                {
                    "@type": "schema:Person",
                    "schema:name": "Analytica, Maria",
                    "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
                    "schema:affiliation": {
                        "@type": "schema:Organization",
                        "schema:name": "Lunar and Planetary Institute",
                    },
                    "schema:contactPoint": {
                        "@type": "schema:ContactPoint",
                        "schema:email": "analytica@example.org",
                    },
                },
                {
                    "@type": "schema:Person",
                    "schema:name": "Researcher, John Q.",
                    "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
                    "schema:affiliation": {
                        "@type": "schema:Organization",
                        "schema:name": "NASA Johnson Space Center",
                    },
                },
            ],
        },
        "schema:contributor": [
            {
                "@type": "schema:Role",
                "schema:roleName": "principalInvestigator",
                "schema:contributor": {
                    "@type": "schema:Person",
                    "schema:name": "Leadscientist, Patricia",
                    "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
                    "schema:contactPoint": {
                        "@type": "schema:ContactPoint",
                        "schema:email": "leadscientist@example.org",
                    },
                },
            },
        ],
        "schema:funding": [
            {
                "@type": "schema:MonetaryGrant",
                "schema:identifier": "NNX17AE48G",
                "schema:name": "Astromaterials Curation and Analysis",
                "schema:funder": {
                    "@type": "schema:Organization",
                    "schema:additionalType": ["schema:FundingAgency"],
                    "schema:name": "NASA",
                },
            },
        ],
        "schema:measurementTechnique": {
            "@type": "schema:DefinedTerm",
            "schema:name": full,
            "schema:identifier": f"https://ada.astromat.org/vocabulary/techniques/{short}",
        },
        "prov:wasGeneratedBy": [
            {
                "@type": ["prov:Activity", "schema:Event"],
                "schema:identifier": f"session-{short.lower()}-20260110-001",
                "schema:startDate": "2026-01-10T09:30:00",
                "prov:used": [
                    {
                        "@type": [
                            "schema:Thing",
                            "prov:Entity",
                            "nxs:BaseClass/NXinstrument",
                        ],
                        "schema:additionalType": [f"ada:{short}Instrument"],
                        "schema:name": f"Example {short} Instrument",
                        "schema:identifier": f"ex:instrument-{short.lower()}-001",
                    },
                ],
                "schema:location": {
                    "@type": ["schema:Place", "nxs:BaseClass/NXsource"],
                    "schema:name": "Analytical Sciences Laboratory",
                    "schema:identifier": "https://ror.org/00hx57361",
                },
                "schema:mainEntity": [
                    {
                        "@type": [
                            "schema:Thing",
                            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
                        ],
                        "schema:additionalType": ["MaterialSample"],
                        "schema:name": "ALH 84001,123",
                        "schema:identifier": ["igsn:10.60471/GSEEXAMPLE001"],
                        "schema:description": "Thin section of Allan Hills 84001 martian meteorite",
                    },
                ],
            },
        ],
        "schema:variableMeasured": [
            {
                "@id": f"ex:{profile_name}-var-001",
                "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
                "schema:name": "measurement_value",
                "schema:alternateName": [f"{short} primary measurement"],
                "schema:description": (
                    f"Primary measured quantity from {full} analysis. "
                    f"This is example mock data for testing."
                ),
                "schema:propertyID": [
                    f"https://ada.astromat.org/vocabulary/variables/{short.lower()}_primary",
                ],
                "schema:unitText": "counts",
                "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
                "cdi:role": "MeasureComponent",
                "cdi:simpleUnitOfMeasure": "counts",
            },
            {
                "@id": f"ex:{profile_name}-var-002",
                "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
                "schema:name": "position_x",
                "schema:alternateName": ["X coordinate"],
                "schema:description": "Horizontal position coordinate on sample surface.",
                "schema:propertyID": [
                    "https://ada.astromat.org/vocabulary/variables/position_x",
                ],
                "schema:unitText": "micrometer",
                "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
                "cdi:role": "DimensionComponent",
                "cdi:simpleUnitOfMeasure": "um",
            },
        ],
        "schema:distribution": [
            {
                "@type": ["schema:DataDownload"],
                "schema:name": f"{profile_name}-ALH84001-archive.zip",
                "schema:description": (
                    f"Archive containing {short} data files and supplementary materials"
                ),
                "schema:contentUrl": (
                    f"https://astromat.org/downloads/{profile_name.lower()}-example-001.zip"
                ),
                "schema:encodingFormat": ["application/zip"],
                "schema:additionalType": ["RO-CRATE"],
                "spdx:checksum": {
                    "spdx:algorithm": "SHA256",
                    "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
                },
                "schema:size": {
                    "@type": "schema:QuantitativeValue",
                    "schema:value": 15728640,
                    "schema:unitText": "byte",
                },
                "schema:provider": [
                    {
                        "@type": "schema:Organization",
                        "schema:name": "Astromat Data Archive",
                    },
                ],
                "schema:hasPart": [
                    {
                        "@id": f"ex:{profile_name}-file-001",
                        "@type": ["ada:image", "schema:ImageObject"],
                        "schema:name": f"ALH84001_{short}_001.tif",
                        "schema:description": f"{short} data file for ALH 84001 thin section",
                        "schema:additionalType": [f"ada:{first_ct}"],
                        "schema:encodingFormat": ["image/tiff"],
                        "schema:size": {
                            "@type": "schema:QuantitativeValue",
                            "schema:value": 10485760,
                            "schema:unitText": "byte",
                        },
                        "spdx:checksum": {
                            "spdx:algorithm": "MD5",
                            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e",
                        },
                        "componentType": {
                            "@type": f"ada:{first_ct}",
                        },
                    },
                    {
                        "@id": f"ex:{profile_name}-file-002",
                        "@type": ["ada:document", "schema:DigitalDocument"],
                        "schema:name": f"ALH84001_{short}_methods.pdf",
                        "schema:description": "Method description document for this analysis",
                        "schema:additionalType": [f"ada:{supporting_ct}"],
                        "schema:encodingFormat": ["application/pdf"],
                        "schema:size": {
                            "@type": "schema:QuantitativeValue",
                            "schema:value": 524288,
                            "schema:unitText": "byte",
                        },
                        "componentType": {
                            "@type": f"ada:{supporting_ct}",
                        },
                    },
                ],
            },
        ],
        "schema:subjectOf": {
            "@type": "schema:Dataset",
            "@id": f"ex:{profile_name}-metadata-001",
            "schema:about": {"@id": f"ex:{profile_name}-example-001"},
            "schema:dateModified": "2026-01-15",
            "dcterms:conformsTo": [
                {"@id": "https://w3id.org/cdif/profiles/discovery"},
                {"@id": f"https://ada.astromat.org/profiles/{profile_name}"},
            ],
            "schema:maintainer": {
                "@type": "schema:Organization",
                "schema:name": "Astromat Data Archive",
            },
            "schema:sdDatePublished": "2026-01-15T12:00:00Z",
            "schema:includedInDataCatalog": {
                "@type": "schema:DataCatalog",
                "schema:name": "Astromat Data Archive",
                "schema:url": "https://astromat.org",
            },
        },
    }

    return example


# ---------------------------------------------------------------------------
# examples.yaml updater
# ---------------------------------------------------------------------------

def update_examples_yaml(profile_dir: Path, profile_name: str, cfg: dict) -> None:
    """Update examples.yaml to reference the example JSON file."""
    short = cfg["short_name"]
    json_filename = f"example{profile_name}.json"

    content = f"""- title: {short} Product Example
  content: |-
    Example {cfg['full_name']} product metadata with all properties populated.
    Mock data for validation and testing.
  prefixes:
    schema: http://schema.org/
    ada: https://ada.astromat.org/metadata/
    cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
    prov: http://www.w3.org/ns/prov#
    dcterms: http://purl.org/dc/terms/
  snippets:
    - language: json
      ref: {json_filename}
"""
    yaml_path = profile_dir / "examples.yaml"
    yaml_path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate example JSON-LD instances for ADA profiles",
    )
    parser.add_argument(
        "profiles",
        nargs="*",
        help="Profile names to generate (default: all missing)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Regenerate all examples (overwrite existing)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List profiles that need examples",
    )
    parser.add_argument(
        "--no-yaml",
        action="store_true",
        help="Skip updating examples.yaml files",
    )
    args = parser.parse_args()

    all_profiles = get_all_ada_profiles()

    if args.list:
        for name in sorted(all_profiles.keys()):
            profile_dir = PROFILES_DIR / name
            json_file = profile_dir / f"example{name}.json"
            status = "EXISTS" if json_file.exists() else "MISSING"
            print(f"  {name:20s}  {status}")
        return

    # Determine which profiles to process
    if args.profiles:
        to_generate = {}
        for name in args.profiles:
            if name not in all_profiles:
                print(f"ERROR: Unknown profile '{name}'", file=sys.stderr)
                print(
                    f"Available: {', '.join(sorted(all_profiles.keys()))}",
                    file=sys.stderr,
                )
                sys.exit(1)
            to_generate[name] = all_profiles[name]
    else:
        to_generate = all_profiles

    generated = 0
    skipped = 0

    for name in sorted(to_generate.keys()):
        cfg = to_generate[name]
        profile_dir = PROFILES_DIR / name
        json_file = profile_dir / f"example{name}.json"

        if not profile_dir.exists():
            print(f"  SKIP {name} (directory not found)", file=sys.stderr)
            skipped += 1
            continue

        if json_file.exists() and not args.all:
            print(f"  SKIP {name} (already exists)", file=sys.stderr)
            skipped += 1
            continue

        # Generate the example
        example = build_example(name, cfg)
        json_text = json.dumps(example, indent=4, ensure_ascii=False) + "\n"
        json_file.write_text(json_text, encoding="utf-8")

        # Update examples.yaml
        if not args.no_yaml:
            update_examples_yaml(profile_dir, name, cfg)

        print(f"  Generated {name}/example{name}.json")
        generated += 1

    print(
        f"\nDone: {generated} generated, {skipped} skipped",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
