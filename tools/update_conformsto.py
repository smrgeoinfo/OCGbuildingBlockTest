#!/usr/bin/env python3
"""
Update dcterms:conformsTo in ADA JSON-LD metadata files to declare the
correct profile based on schema:measurementTechnique.schema:termCode.

Replaces the generic conformsTo entries (e.g. "ada:metadata", "CDIF_basic_1.0")
with the standardised profile URIs:
    [
      {"@id": "https://w3id.org/cdif/profiles/discovery"},
      {"@id": "ada:profile/{profileName}"}
    ]

Usage:
    # Dry-run (preview changes without writing)
    python tools/update_conformsto.py /path/to/testJSONMetadata --dry-run

    # Verbose dry-run
    python tools/update_conformsto.py /path/to/testJSONMetadata --dry-run -v

    # Apply changes
    python tools/update_conformsto.py /path/to/testJSONMetadata

    # Verbose apply
    python tools/update_conformsto.py /path/to/testJSONMetadata -v
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CDIF_DISCOVERY_URI = "https://w3id.org/cdif/profiles/discovery"
ADA_PROFILE_PREFIX = "ada:profile/"

TERMCODE_TO_PROFILE = {
    "AIVA": "adaAIVA",
    "AMS": "adaAMS",
    "ARGT": "adaARGT",
    "DSC": "adaDSC",
    "EA-IRMS": "adaEAIRMS",
    "EMPA": "adaEMPA",
    "FIB-SEM": "adaSEM",
    "FTICR-MS": "adaFTICRMS",
    "GC-MS": "adaGCMS",
    "GPYC": "adaGPYC",
    "HR-ICP-MS": "adaICPMS",
    "IC": "adaIC",
    "ICP-OES": "adaICPOES",
    "LAF": "adaLAF",
    "LC-MS": "adaLCMS",
    "LIT": "adaLIT",
    "MC-ICP-MS": "adaICPMS",
    "NanoIR": "adaNanoIR",
    "NanoSIMS": "adaNanoSIMS",
    "NG-NS-MS": "adaNGNSMS",
    "PSFD": "adaPSFD",
    "Q-ICP-MS": "adaICPMS",
    "QRIS": "adaQRIS",
    "RAMAN": "adaRAMAN",
    "RI-TOF-NGMS": "adaRITOFNGMS",
    "SEM": "adaSEM",
    "SIMS": "adaSIMS",
    "SLS": "adaSLS",
    "SV-RUEC": "adaSVRUEC",
    "TEM": "adaTEM",
    "ToF-SIMS": "adaToFSIMS",
    "uL2MS": "adaL2MS",
    "UVFM": "adaUVFM",
    "VLM": "adaVLM",
    "VLMBasemap": "adaVLM",
    "VNMIR": "adaVNMIR",
    "XANES": "adaXANES",
    "XCT": "adaXCT",
    "XRD": "adaXRD",
}
DEFAULT_PROFILE = "adaProduct"


def get_profile(data: dict) -> tuple[str, str]:
    """
    Determine the profile for a metadata file.

    Returns (profile_name, term_code).
    """
    mt = data.get("schema:measurementTechnique", {})
    term_code = mt.get("schema:termCode", "")
    profile = TERMCODE_TO_PROFILE.get(term_code, DEFAULT_PROFILE)
    return profile, term_code


def build_conformsto(profile_name: str) -> list[dict]:
    """Build the new dcterms:conformsTo value."""
    return [
        {"@id": CDIF_DISCOVERY_URI},
        {"@id": f"{ADA_PROFILE_PREFIX}{profile_name}"},
    ]


def update_file(filepath: Path, *, dry_run: bool = False, verbose: bool = False) -> tuple[str, str]:
    """
    Update conformsTo in a single file.

    Returns (term_code, profile_name).
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    profile, term_code = get_profile(data)
    new_conformsto = build_conformsto(profile)

    if verbose:
        old = data.get("schema:subjectOf", {}).get("dcterms:conformsTo", [])
        old_ids = [e.get("@id", str(e)) if isinstance(e, dict) else str(e) for e in old]
        print(f"  {filepath.name}: {term_code} -> {profile}")
        print(f"    old: {old_ids}")
        print(f"    new: [{CDIF_DISCOVERY_URI}, {ADA_PROFILE_PREFIX}{profile}]")

    # Update the data
    if "schema:subjectOf" not in data:
        data["schema:subjectOf"] = {}
    data["schema:subjectOf"]["dcterms:conformsTo"] = new_conformsto

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

    return term_code, profile


def main():
    parser = argparse.ArgumentParser(
        description="Update dcterms:conformsTo in ADA metadata files to "
                    "declare the correct profile URI."
    )
    parser.add_argument(
        "metadata_dir",
        help="Directory containing JSON-LD metadata files."
    )
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Preview changes without writing files."
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show details for each file."
    )

    args = parser.parse_args()
    metadata_dir = Path(args.metadata_dir)

    if not metadata_dir.is_dir():
        sys.exit(f"Not a directory: {metadata_dir}")

    files = sorted(metadata_dir.glob("*.json"))
    if not files:
        sys.exit(f"No JSON files found in {metadata_dir}")

    if args.dry_run:
        print("DRY RUN — no files will be modified\n")

    profile_counts: Counter = Counter()
    errors = []

    for fp in files:
        try:
            term_code, profile = update_file(
                fp, dry_run=args.dry_run, verbose=args.verbose
            )
            profile_counts[profile] += 1
            if not args.verbose:
                print(f"{fp.name}: {term_code} -> {profile}")
        except (json.JSONDecodeError, KeyError, OSError) as exc:
            errors.append((fp.name, str(exc)))
            print(f"{fp.name}: ERROR — {exc}", file=sys.stderr)

    # Summary
    print(f"\nSummary: {len(files)} files", end="")
    if errors:
        print(f" ({len(errors)} errors)", end="")
    print()
    for profile in sorted(profile_counts.keys()):
        print(f"  {profile}: {profile_counts[profile]}")

    if args.dry_run:
        print("\n(dry run — no files were modified)")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
