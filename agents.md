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
├── tools/
│   ├── resolve_schema.py            # Schema resolver (see below)
│   ├── convert_for_jsonforms.py     # JSON Forms converter (see below)
│   ├── augment_register.py          # Adds resolvedSchema URLs to register.json
│   └── cors_server.py               # CORS dev server for local testing
└── .github/workflows/               # Validation + JSON Forms generation
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
│   ├── Branch 1: single file (files + @type contains DataDownload)
│   │   ├── spdx:checksum → {spdx:algorithm, spdx:checksumValue}
│   │   ├── schema:encodingFormat → array of strings
│   │   └── fileDetail → anyOf [image, imageMap, tabularData, ...]
│   ├── Branch 2: archive (files + DataDownload + schema:hasPart)
│   │   └── schema:hasPart → items (files + NOT DataDownload)
│   │       └── allOf: [common file props] + anyOf [file type BBs]
│   │           ├── image (componentType enum)
│   │           ├── imageMap (componentType: empa_detail or enum)
│   │           ├── supDocImage (componentType enum, incl. ada:other)
│   │           ├── tabularData (TabularTextDataSet + CSVW + oneOf delimited/fixedWidth)
│   │           │   └── cdi:hasPhysicalMapping → physicalMapping (flat per-column)
│   │           ├── collection (componentType enum + filelist + nFiles)
│   │           ├── dataCube (StructuredDataSet + hasPhysicalMapping + locator)
│   │           ├── document (componentType enum + schema:version, schema:isBasedOn)
│   │           └── otherFile (componentType + encodingFormat enum)
│   └── Branch 3: WebAPI (schema:WebAPI)
│       ├── schema:serviceType, schema:documentation, schema:termsOfService
│       └── schema:potentialAction → action (schema:Action)
│           └── schema:result → oneOf [single file, archive] (reuses Branches 1 & 2)
└── schema:subjectOf → metadata record
```

### Technique Profiles

Technique profiles extend `adaProduct` via `allOf` and constrain both component types (`schema:additionalType`) and file types (`fileDetail`) to those valid for the technique:

```
profiles/adaEMPA/    ← extends adaProduct
├── schema:additionalType contains EMPA product type
├── schema:distribution hasPart additionalType constrained to:
│   EMPAImageMap, EMPAImage, EMPAQEATabular, EMPAImageCollection,
│   analysisLocation, supplementaryImage, calibrationFile, methodDescription,
│   instrumentMetadata
└── fileDetail anyOf: imageMap, image, tabularData, collection, supDocImage, document

profiles/adaXRD/     ← extends adaProduct
├── schema:additionalType contains XRD product type
├── schema:distribution hasPart additionalType constrained to:
│   XRDTabular, XRDDiffractionPattern, XRDIndexedImage,
│   instrumentMetadata, methodDescription
└── fileDetail anyOf: tabularData, image, document

profiles/adaICPMS/   ← extends adaProduct
├── schema:additionalType contains ICP-MS product type (HR/Q/MC variants)
├── schema:distribution hasPart additionalType constrained to:
│   HRICPMSProcessed, HRICPMSRaw, QICPMSProcessedTabular, QICPMSRawTabular,
│   MCICPMSTabular, MCICPMSCollection, MCICPMSRaw, methodDescription,
│   instrumentMetadata, calibrationFile
└── fileDetail anyOf: tabularData, collection, document

profiles/adaVNMIR/   ← extends adaProduct
├── schema:additionalType contains VNMIR product type
├── schema:distribution hasPart additionalType constrained to:
│   VNMIRSpectralPoint, VNMIROverviewImage, VNMIRSpectralMap,
│   VNMIRSpectraPlot, analysisLocation, instrumentMetadata, methodDescription
└── fileDetail anyOf: tabularData, imageMap, dataCube, supDocImage, document
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

# Schema Tools

## Schema Pipeline

Three tools transform modular YAML source schemas into JSON Forms-compatible Draft 7 schemas and augment the bblocks-viewer register:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                                       → augment_register.py → register.json (adds resolvedSchema URLs)
```

## resolve_schema.py

Recursively resolves ALL `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. No external references remain in the output — all `$defs` are inlined and removed.

**$ref patterns handled:**
1. Relative path: `$ref: ../detailEMPA/schema.yaml`
2. Fragment-only: `$ref: '#/$defs/Identifier'`
3. Cross-file fragment: `$ref: ../metaMetadata/schema.yaml#/$defs/conformsTo_item`
4. Both YAML and JSON file extensions

**Usage:**
```bash
# Resolve a profile by name (looks in _sources/profiles/{name}/schema.yaml)
python tools/resolve_schema.py adaProduct
python tools/resolve_schema.py adaEMPA --flatten-allof -o _sources/profiles/adaEMPA/resolvedSchema.json

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml

# Resolve all profiles
for p in adaProduct adaEMPA adaICPMS adaVNMIR adaXRD CDIFDiscovery; do
  python tools/resolve_schema.py $p --flatten-allof -o _sources/profiles/$p/resolvedSchema.json
done
```

**CLI options:** `profile` (positional, profile name), `--file` (arbitrary schema path), `-o`/`--output` (output file, default: stdout), `--flatten-allof` (merge allOf entries into single objects).

**Requirements:** Python 3.6+ with `pyyaml`

**Key implementation details:**
- `deep_merge` with `_is_complete_schema` heuristic: when merging `properties` dicts, overlay properties with `type`/`oneOf`/`anyOf`/`allOf`/`$ref` **replace** the base entirely; partial constraint patches (no composition keywords) are deep-merged
- Two-pass `$defs` resolution: pass 1 resolves external file refs with empty defs dict, pass 2 uses `_inline_unresolved_defs` to replace `$comment` placeholders left by forward cross-def fragment refs
- Circular reference detection via `seen` set (returns `$comment` placeholder)
- Strips metadata keys (`$id`, `x-jsonld-*`) from output

## convert_for_jsonforms.py

Reads `resolvedSchema.json` (from `_sources/profiles/{name}/`) and converts to JSON Forms-compatible Draft 7:
- Converts `$schema` from Draft 2020-12 to Draft 7
- Simplifies `anyOf` patterns for form rendering (single-item anyOf unwrapped, duplicate removal)
- Converts `contains` → `enum`, `const` → `default`
- Merges technique profile constraints into distribution `oneOf` branches
- Preserves `oneOf` in distribution (3 branches: single file, archive, WebAPI)
- Preserves `anyOf` in fileDetail (technique-specific file type subsets)
- Removes `not` constraints and relaxes `minItems`

**Usage:**
```bash
python tools/convert_for_jsonforms.py adaProduct -v
python tools/convert_for_jsonforms.py --all -v
```

**Output:** `build/jsonforms/profiles/{name}/schema.json`

## augment_register.py

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block. Scans bblock identifiers for `.profiles.{name}` patterns and checks whether `_sources/profiles/{name}/resolvedSchema.json` exists. If so, adds the GitHub Pages URL as `bblock.resolvedSchema`.

**Usage:**
```bash
python tools/augment_register.py
```

**Why:** The bblocks-viewer fork has a "Resolved (JSON)" button in the JSON Schema tab that fetches the resolved schema from this URL. The OGC postprocessor doesn't know about `resolvedSchema.json`, so this script injects the URLs after the postprocessor generates `register.json`.

**Workflow integration:** The `generate-jsonforms` workflow runs this after `convert_for_jsonforms.py` and stages `build/register.json` alongside `build/jsonforms/`.

## Verification

```bash
# Verify distribution has oneOf only (no conflicting anyOf)
python -c "
import json
with open('_sources/profiles/adaProduct/resolvedSchema.json') as f:
    s = json.load(f)
items = s['properties']['schema:distribution']['items']
assert 'oneOf' in items, 'Missing oneOf'
assert 'anyOf' not in items, 'Conflicting anyOf still present'
print(f'Distribution OK: {len(items[\"oneOf\"])} branches')
"
```

## License

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
