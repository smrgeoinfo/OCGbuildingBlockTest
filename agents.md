# Agents Guide: OGC Building Blocks Repository

This document explains how to work with this repository — the building block structure, authoring rules, validation workflow, and the schema resolver tool.

## What This Repository Is

This repository contains modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern. Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

The repository is included as a git submodule in the [IEDA Data Submission Portal](https://github.com/smrgeoinfo/IEDADataSubmission) monorepo.

## Repository Structure

```
OCGbuildingBlockTest/
├── _sources/                        # All building block sources
│   ├── schemaorgProperties/         # Core schema.org property types
│   │   ├── person/                  # schema:Person
│   │   ├── organization/            # schema:Organization
│   │   ├── identifier/              # schema:identifier (PropertyValue)
│   │   ├── definedTerm/             # schema:DefinedTerm
│   │   ├── additionalProperty/      # schema:PropertyValue for soft-typed properties
│   │   ├── variableMeasured/        # schema:variableMeasured (PropertyValue)
│   │   ├── spatialExtent/           # schema:Place (bounding box)
│   │   ├── temporalExtent/          # schema:temporalCoverage
│   │   ├── dataDownload/            # schema:DataDownload
│   │   ├── labeledLink/             # schema:LinkRole
│   │   ├── funder/                  # schema:funder / schema:Grant
│   │   ├── webAPI/                  # schema:WebAPI
│   │   ├── action/                  # schema:Action
│   │   ├── agentInRole/             # schema:Role wrapping Person/Org
│   │   ├── metaMetadata/            # dcterms:conformsTo metadata-about-metadata
│   │   ├── cdifMandatory/           # CDIF mandatory property group
│   │   └── cdifOptional/            # CDIF optional property group
│   ├── adaProperties/               # ADA (Astromat Data Archive) property types
│   │   ├── stringArray/             # Reusable string array utility type
│   │   ├── creativeWork/            # schema:CreativeWork labeled links
│   │   ├── spatialRegistration/     # Pixel coordinate system registration
│   │   ├── instrument/              # NXinstrument + prov:Entity analytical instruments
│   │   ├── laboratory/              # NXsource + schema:Place facilities
│   │   ├── details/                 # 16 instrument-specific detail types ($defs)
│   │   ├── physicalMapping/         # DDI-CDI flat per-column variable mapping (CDIF 2026)
│   │   ├── image/                   # ada:image with componentType classification
│   │   ├── imageMap/                # Spatially registered image maps
│   │   ├── supDocImage/             # Supplemental document images
│   │   ├── tabularData/             # CDI TabularTextDataSet with CSVW properties (CDIF 2026)
│   │   ├── collection/              # Sets of related files
│   │   ├── dataCube/                # CDI StructuredDataSet multidimensional data (CDIF 2026)
│   │   ├── document/                # Supplemental documents (calibration, methods, logs)
│   │   ├── otherFile/               # Non-standard file formats (EMSA, OBJ, STL, XLSX)
│   │   └── files/                   # File-level metadata (generic, type constraints at profile level)
│   ├── provProperties/              # W3C PROV provenance types
│   │   ├── generatedBy/             # prov:wasGeneratedBy (Activity)
│   │   └── derivedFrom/             # prov:wasDerivedFrom
│   ├── cdiProperties/               # DDI-CDI data description types
│   │   └── cdiVariableMeasured/     # CDI variable measured extension
│   ├── qualityProperties/           # Data quality types
│   │   └── qualityMeasure/          # Quality measure definitions
│   ├── xasProperties/               # X-ray Absorption Spectroscopy types
│   │   ├── xasSample/               # XAS sample (extends schema:Product)
│   │   ├── xasInstrument/           # XAS instrument (beamline, synchrotron)
│   │   ├── xasFacility/             # XAS facility (synchrotron source)
│   │   ├── xasGeneratedBy/          # XAS analysis event (extends prov:Activity)
│   │   ├── xasHDF5DataStructure/    # HDF5 data structure for XAS
│   │   ├── xasXdiTabularTextDataset/ # XDI tabular text dataset
│   │   ├── xasRequired/             # XAS mandatory property group
│   │   ├── xasOptional/             # XAS optional property group
│   │   └── xasSubject/              # XAS subject classification
│   └── profiles/                    # Top-level profiles that compose BBs
│       ├── CDIFDiscovery/           # CDIF Discovery profile
│       ├── adaProduct/              # ADA product metadata profile (v3, CDIF 2026)
│       ├── adaEMPA/                 # Electron Microprobe Analysis technique profile
│       ├── adaXRD/                  # X-ray Diffraction technique profile
│       ├── adaICPMS/                # ICP Mass Spectrometry technique profile
│       └── adaVNMIR/                # Very-Near Mid-IR / FTIR spectroscopy profile
├── resolve_schema.py                # Schema resolver tool (see below)
└── .github/workflows/               # Validation workflow
```

## Building Block Structure

Each building block directory contains:

| File | Required | Purpose |
|---|---|---|
| `bblock.json` | Yes | Metadata: name, status, tags, version, links, sources |
| `schema.yaml` | Yes | JSON Schema with `$ref` cross-references to other BBs |
| `context.jsonld` | Yes | JSON-LD namespace prefix mappings |
| `description.md` | Yes | Human-readable description |
| `examples.yaml` | No | Example snippets with `ref:` pointing to example JSON files |

### `bblock.json` Required Fields

Every `bblock.json` must include all of these fields:

```json
{
  "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/refs/heads/master/ogc/bblocks/metadata-schema.yaml",
  "name": "Human-readable name",
  "abstract": "One-line description",
  "status": "under-development",
  "dateTimeAddition": "2026-01-01T00:00:00Z",
  "itemClass": "schema",
  "register": "ogc-building-block",
  "version": "0.1",
  "dateOfLastChange": "2026-01-01",
  "link": "https://github.com/smrgeoinfo/OCGbuildingBlockTest",
  "maturity": "development",
  "scope": "unstable",
  "tags": ["tag1", "tag2"],
  "sources": []
}
```

Missing `dateOfLastChange` or `link` will cause the validation workflow to fail.

### `schema.yaml` Cross-Reference Rules

Schemas reference other building blocks using relative `$ref` paths:

```yaml
$defs:
  Person:
    $ref: ../../schemaorgProperties/person/schema.yaml
  Identifier:
    $ref: ../../schemaorgProperties/identifier/schema.yaml
```

**Critical rules:**

1. **Always reference `schema.yaml`, never standalone `.json` files.** The postprocess tool resolves `$ref` to GitHub Pages URLs. References to `.json` files cause 404 errors because only `schema.yaml` files are published to GitHub Pages.

   ```yaml
   # CORRECT
   $ref: ../../schemaorgProperties/metaMetadata/schema.yaml

   # WRONG — will cause 404 in validation
   $ref: ../../schemaorgProperties/metaMetadata/metaMetadataSchema.json
   ```

2. **Use correct relative paths.** Paths are relative to the current `schema.yaml` file. Building blocks in `xasProperties/` that reference `schemaorgProperties/` need `../../schemaorgProperties/...`, not `../...`.

3. **Reference `$defs` within another schema.yaml** using fragment syntax:
   ```yaml
   $ref: ../../schemaorgProperties/additionalProperty/schema.yaml#/$defs/propertyID_item
   ```

### `examples.yaml` Rules

1. **`ref:` must match the actual filename** in the building block directory. Copy-paste errors referencing files from other BBs (e.g., `exampleWebAPI.json` in a non-webAPI BB) will cause validation failures.

2. **Schema prefix must use `http`, not `https`**, with a trailing slash:
   ```yaml
   # CORRECT
   prefixes:
     schema: http://schema.org/

   # WRONG
   prefixes:
     schema: https://schema.org
   ```

## Validation Workflow

A GitHub Actions workflow (`Validate and process Building Blocks`) runs on every push. It uses the `ogc/bblocks/postprocess` Docker container to:

1. Validate all `bblock.json` files have required fields
2. Resolve all `$ref` paths in `schema.yaml` files
3. Fetch resolved references from GitHub Pages URLs
4. Validate examples against their schemas
5. Generate annotated schemas and documentation

If the workflow fails, check the error log for:
- Missing `bblock.json` fields (especially `dateOfLastChange`, `link`)
- 404 errors fetching resolved `$ref` URLs (usually means a `.json` reference instead of `schema.yaml`)
- `FileNotFoundError` for example files (wrong `ref:` in `examples.yaml`)
- Date format errors (must be `YYYY-MM-DD`, not e.g. `2025-11=04`)

## Vocabulary Namespaces

| Prefix | URI | Used In |
|---|---|---|
| `schema` | `http://schema.org/` | Core metadata (name, description, identifier) — all BBs |
| `ada` | `https://ada.astromat.org/metadata/` | ADA-specific types and properties |
| `cdi` | `http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/` | Data structure descriptions |
| `prov` | `http://www.w3.org/ns/prov#` | Provenance (instruments, activities) |
| `nxs` | `http://purl.org/nexusformat/definitions/` | NeXus instrument/source classes |
| `csvw` | `http://www.w3.org/ns/csvw#` | Tabular data descriptions |
| `spdx` | `http://spdx.org/rdf/terms#` | File checksums |
| `dcterms` | `http://purl.org/dc/terms/` | Conformance declarations |
| `geosparql` | `http://www.opengis.net/ont/geosparql#` | Spatial geometry types |

## ADA Building Blocks

The ADA (Astromat Data Archive) metadata schema (37 `$defs` from `adaMetadata-SchemaOrgSchema-v3.json`, aligned with CDIF 2026 / DDI-CDI / CSVW) has been decomposed into 18 modular building blocks in `adaProperties/` plus 5 profiles in `profiles/` (adaProduct + 4 technique-specific profiles).

### Composition Hierarchy

```
profiles/adaProduct/                    ← Top-level ADA product profile (v3, CDIF 2026)
├── schema:creator → @list of person, organization
├── schema:contributor → person, organization, schema:Role
├── schema:funding → funder (organization, @id ref)
├── schema:identifier → identifier (PropertyValue, string, array)
├── schema:license → creativeWork
├── schema:variableMeasured → variable_type (dual: PropertyValue + cdi:InstanceVariable)
│   └── cdi:role, cdi:intendedDataType, cdi:uses, cdi:describedUnitOfMeasure, etc.
├── prov:wasGeneratedBy → array of analysis events
│   ├── @type: allOf [prov:Activity, schema:Event]
│   ├── prov:used → instrument
│   ├── schema:location → laboratory
│   └── schema:mainEntity → (sample inline, identifier as array)
├── schema:distribution → oneOf:
│   ├── files_type (single file, @type contains DataDownload)
│   │   ├── spdx:checksum → {spdx:algorithm, spdx:checksumValue}
│   │   ├── schema:encodingFormat → array of strings
│   │   └── fileDetail → anyOf [image, imageMap, tabularData, ...]
│   └── archive (DataDownload + schema:hasPart)
│       └── schema:hasPart → hasPart_file_type (NOT DataDownload)
│           └── allOf: [common file props] + anyOf [file type BBs]
│               ├── image (componentType enum)
│               ├── imageMap (componentType: empa_detail or enum)
│               ├── supDocImage (componentType enum, incl. ada:other)
│               ├── tabularData (TabularTextDataSet + CSVW + oneOf delimited/fixedWidth)
│               │   └── cdi:hasPhysicalMapping → physicalMapping (flat per-column)
│               ├── collection (componentType enum + filelist + nFiles)
│               ├── dataCube (StructuredDataSet + hasPhysicalMapping + locator)
│               ├── document (componentType enum + schema:version, schema:isBasedOn)
│               └── otherFile (componentType + encodingFormat enum)
└── schema:subjectOf → metadata record
```

### Technique Profiles

Technique profiles extend `adaProduct` and constrain component types to those valid for the technique:

```
profiles/adaEMPA/    ← extends adaProduct
├── schema:additionalType contains EMPA product type
└── schema:distribution hasPart constrained to:
    EMPAImageMap, EMPAImage, EMPAQEATabular, EMPAImageCollection,
    analysisLocation, supplementaryImage, calibrationFile, methodDescription,
    instrumentMetadata

profiles/adaXRD/     ← extends adaProduct
├── schema:additionalType contains XRD product type
└── schema:distribution hasPart constrained to:
    XRDTabular, XRDDiffractionPattern, XRDIndexedImage,
    instrumentMetadata, methodDescription

profiles/adaICPMS/   ← extends adaProduct
├── schema:additionalType contains ICP-MS product type (HR/Q/MC variants)
└── schema:distribution hasPart constrained to:
    HRICPMSProcessed, HRICPMSRaw, QICPMSProcessedTabular, QICPMSRawTabular,
    MCICPMSTabular, MCICPMSCollection, MCICPMSRaw, methodDescription,
    instrumentMetadata, calibrationFile

profiles/adaVNMIR/   ← extends adaProduct
├── schema:additionalType contains VNMIR product type
└── schema:distribution hasPart constrained to:
    VNMIRSpectralPoint, VNMIROverviewImage, VNMIRSpectralMap,
    VNMIRSpectraPlot, analysisLocation, instrumentMetadata, methodDescription
```

### Detail Types

The `details/` building block contains 16 instrument-specific detail type definitions as `$defs`. 12 are aligned with v3 source schema; 4 are extensions (marked with *):

```
v3-aligned (12):
  argt_detail, dsc_detail, empa_detail, eairms_detail, l2ms_detail,
  laf_detail, nanoir_detail, nanosims_detail, psfd_detail, vnmir_detail,
  slsshapemodel_detail, xrd_detail

Extensions (4):
  basemap_detail*, icpoes_detail*, qris_detail*, xctimage_detail*
```

Referenced as: `../details/schema.yaml#/$defs/empa_detail`

Key detail types used in technique profiles:
- **empa_detail**: `spectrometersUsed`, `signalUsed` (used in adaEMPA)
- **xrd_detail**: `geometry`, `sampleMount`, `stepSize`, `timePerStep`, `wavelength` (used in adaXRD)
- **vnmir_detail**: 20+ properties including `detector`, `beamsplitter`, `spectralRangeMin/Max`, etc. (used in adaVNMIR)
- ICP-MS has no detail type; component types are enum-only

### Integration with CZ Net Portal

The ADA building blocks define the JSON-LD schema structure. The CZ Net Data Submission Portal (`dspback`) has a JSON-LD translation endpoint (`POST /api/metadata/ada/jsonld`) that accepts JSON-LD conforming to the `adaProduct` profile and translates it to the flat format used by the portal's form schema (`schema.json`). See the [IEDADataSubmission agents.md](https://github.com/smrgeoinfo/IEDADataSubmission/blob/main/agents.md) for translation details.

---

# JSON Schema Reference Resolver

## Overview

The `resolve_schema.py` script is a Python utility that transforms modular OGC Building Block JSON schemas into standalone, self-contained schemas. It recursively resolves all external `$ref` references and flattens definitions into a single `$defs` section.

## Purpose

OGC Building Blocks use a modular architecture where schemas reference each other using JSON Schema's `$ref` keyword. While this modularity is excellent for maintenance and reusability, some tools and validators require fully resolved, standalone schemas. This tool bridges that gap.

### Before (Modular)
```json
{
  "$defs": {
    "Person": {"$ref": "../person/personSchema.json"},
    "Organization": {"$ref": "../organization/organizationSchema.json"}
  }
}
```

### After (Standalone)
```json
{
  "$defs": {
    "Person": { /* full person schema inlined */ },
    "Organization": { /* full organization schema inlined */ }
  }
}
```

## Installation

No external dependencies required. The script uses only Python standard library modules:
- `json` - JSON parsing and serialization
- `pathlib` - Cross-platform path handling
- `argparse` - Command-line argument parsing
- `copy` - Deep copying of schema objects
- `urllib.parse` - URL fragment parsing

**Requirements:** Python 3.6+

## Usage

### Basic Usage

```bash
# Print resolved schema to stdout
python resolve_schema.py <input_schema_path>

# Save to file
python resolve_schema.py <input_schema_path> -o <output_path>
```

### Examples

```bash
# Resolve the main CDIF Discovery profile
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json

# Save resolved schema to a file
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json -o resolved_cdif.json

# Verbose mode - shows which files are being loaded
python resolve_schema.py _sources/schemaorgProperties/cdifMandatory/cdifMandatorySchema.json -v

# Custom JSON indentation (default is 2)
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json --indent 4
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `input_schema` | Path to the input JSON schema file (required) |
| `-o, --output` | Output file path (default: prints to stdout) |
| `-v, --verbose` | Print progress information to stderr |
| `--indent` | JSON indentation level (default: 2) |
| `--inline-single-use` | Inline definitions that are only referenced once |

## How It Works

### Architecture

The resolver uses a single-pass recursive algorithm with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     SchemaResolver                          │
├─────────────────────────────────────────────────────────────┤
│  schema_cache      Dict[str, dict]   Loaded file cache      │
│  global_defs       Dict[str, dict]   Flattened definitions  │
│  processing_stack  Set[str]          Cycle detection        │
│  file_to_def_name  Dict[str, str]    Path → def name map    │
│  warnings          List[str]         Collected warnings     │
└─────────────────────────────────────────────────────────────┘
```

### Processing Flow

```
1. Load root schema
       │
       ▼
2. Process schema recursively
       │
       ├──► Find $ref → External? ──► Load & process referenced file
       │                    │              │
       │                    │              ▼
       │                    │         Add to global_defs
       │                    │              │
       │                    │              ▼
       │                    └──────► Replace with #/$defs/Name
       │
       ├──► Find $defs → Process each definition
       │                    │
       │                    ▼
       │              Add to global_defs (flattened)
       │
       └──► Process nested objects/arrays recursively
       │
       ▼
3. Merge global_defs into result
       │
       ▼
4. Output standalone schema
```

### Reference Types Handled

The resolver handles all common JSON Schema reference patterns:

| Pattern | Example | Description |
|---------|---------|-------------|
| Relative file | `"$ref": "../person/personSchema.json"` | Reference to another schema file |
| Fragment | `"$ref": "#/$defs/Identifier"` | Internal reference (preserved as-is) |
| File + Fragment | `"$ref": "../file.json#/$defs/Name"` | Reference to specific definition in another file |
| allOf composition | `"allOf": [{"$ref": "..."}]` | Schema composition |

### Key Methods

#### `resolve(schema_path: str) -> dict`
Main entry point. Loads the root schema and initiates processing.

```python
resolver = SchemaResolver(verbose=True)
result = resolver.resolve("path/to/schema.json")
```

#### `process_schema(schema: Any, current_dir: Path) -> Any`
Recursively processes a schema node, handling:
- `$ref` references (external → resolved, internal → preserved)
- `$defs` sections (extracted and flattened)
- Nested objects and arrays

#### `get_or_create_def_for_file(schema_path: Path, fragment: Optional[str]) -> str`
Ensures each external schema is processed only once:
1. Checks cache for existing definition
2. Generates unique name if needed
3. Loads and processes the schema
4. Stores in `global_defs`
5. Returns the definition name

#### `parse_ref(ref: str) -> Tuple[str, Optional[str]]`
Splits a `$ref` value into file path and fragment:
```python
parse_ref("../person/personSchema.json#/$defs/Name")
# Returns: ("../person/personSchema.json", "/$defs/Name")
```

## Features

### Caching
Schemas are loaded once and cached. If multiple schemas reference the same file, it's only read from disk once.

### Cycle Detection
The `processing_stack` tracks schemas currently being processed. If a cycle is detected, the resolver returns a reference to the existing definition instead of infinite recursion.

### Unique Name Generation
When multiple schemas define types with the same name, the resolver generates unique names:
```
Person, Person_2, Person_3, ...
```

### Typo Detection
The resolver detects common typos like using `"$defs"` instead of `"$ref"`:
```json
// This typo is detected and handled:
{"$defs": "../variableMeasured/variableMeasuredSchema.json"}
// Should be:
{"$ref": "../variableMeasured/variableMeasuredSchema.json"}
```

A warning is emitted but processing continues.

### Property Preservation
When a `$ref` has sibling properties (uncommon but valid), they are preserved:
```json
// Input
{"$ref": "../identifier/identifierSchema.json", "description": "Custom desc"}

// Output
{"$ref": "#/$defs/Identifier", "description": "Custom desc"}
```

### Inline Single-Use Definitions

With the `--inline-single-use` flag, the resolver produces a more compact schema by:
1. Keeping definitions in `$defs` only if they are referenced multiple times
2. Inlining definitions that are referenced only once directly where they are used

This produces output similar to hand-authored schemas like `CDIF-JSONLD-schema-schemaprefix.json`.

```bash
python resolve_schema.py schema.json -o output.json --inline-single-use -v
```

Example output (verbose mode):
```
Single-use definitions to inline: {'DataDownload', 'MetaMetadata', 'WebAPI', ...}
Multi-use definitions to keep: {'Person', 'Organization', 'Identifier', 'DefinedTerm', ...}
```

The optimization considers:
- References in the main schema properties
- References within other definitions (if A references B multiple times, B is kept in `$defs`)
- Unreferenced definitions are also inlined (they may be dead code)

## Output Format

The resolved schema has all definitions in a single top-level `$defs` section:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "creator": {"$ref": "#/$defs/Person"}
  },
  "$defs": {
    "Person": { /* ... */ },
    "Organization": { /* ... */ },
    "Identifier": { /* ... */ }
  }
}
```

All external references are converted to internal references:
- Before: `{"$ref": "../person/personSchema.json"}`
- After: `{"$ref": "#/$defs/Person"}`

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `Input file not found` | Schema path doesn't exist | Check the path |
| `Referenced file not found` | A `$ref` points to non-existent file | Fix the reference path |
| `Invalid JSON` | Malformed JSON in a schema file | Fix the JSON syntax |
| `Missing key` | Fragment references non-existent path | Fix the fragment pointer |

Use `-v` (verbose) mode to see the full stack trace for debugging.

## Limitations

1. **HTTP/HTTPS references**: Only local file references are supported. Remote URLs in `$ref` are not fetched.

2. **JSON Schema keywords**: The resolver doesn't validate JSON Schema semantics; it only resolves references.

3. **Circular references**: While detected, complex circular dependencies may result in incomplete definitions.

## Example: Building Block Structure

The resolver is designed for the OGC Building Blocks directory structure:

```
_sources/
├── profiles/
│   └── CDIFDiscovery/
│       └── CDIFDiscoverySchema.json    ← Profile (uses allOf)
├── schemaorgProperties/
│   ├── person/
│   │   └── personSchema.json           ← Component
│   ├── organization/
│   │   └── organizationSchema.json     ← Component
│   └── identifier/
│       └── identifierSchema.json       ← Component
└── provProperties/
    └── generatedBy/
        └── generatedBySchema.json      ← Component
```

Running on the profile:
```bash
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json -v
```

Output shows the dependency resolution:
```
Loading: .../CDIFDiscoverySchema.json
Loading: .../cdifMandatorySchema.json
Loading: .../personSchema.json
Loading: .../organizationSchema.json
Loading: .../identifierSchema.json
...
```

## Programmatic Usage

The resolver can be used as a library:

```python
from resolve_schema import SchemaResolver

# Create resolver
resolver = SchemaResolver(verbose=False)

# Resolve schema
standalone_schema = resolver.resolve("path/to/schema.json")

# Check for warnings
if resolver.warnings:
    print("Warnings:", resolver.warnings)

# Use the resolved schema
import json
print(json.dumps(standalone_schema, indent=2))
```

## Contributing

When modifying the resolver:

1. Test with simple schemas first (e.g., `identifierSchema.json`)
2. Test with complex profiles (e.g., `CDIFDiscoverySchema.json`)
3. Verify no external references remain: `grep '"$ref"' output.json | grep -v '#/$defs/'`
4. Validate the output is valid JSON

## License

This tool is part of the OGC Building Blocks repository. See the repository license for terms.

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
