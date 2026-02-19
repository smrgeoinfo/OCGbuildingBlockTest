# Relationship of ADA/CDIF Metadata Profiles to RO-Crate

## Overview

The [adaProduct](../_sources/profiles/adaProfiles/adaProduct/) and [CDIFcomplete](../_sources/profiles/cdifProfiles/CDIFcomplete/) building block profiles produce JSON-LD metadata that shares a common vocabulary foundation with [RO-Crate](https://www.researchobject.org/ro-crate/) (Research Object Crate). Both systems build on [schema.org](https://schema.org) types and properties to describe datasets, files, people, and organizations. This document describes the property-level correspondences, the structural differences, and how a translator tool converts ADA or CDIF metadata into a conformant `ro-crate-metadata.json`.

## What is RO-Crate?

RO-Crate is a community specification for packaging research data with structured metadata. An RO-Crate is a directory (or archive) containing a `ro-crate-metadata.json` file that describes the dataset and its constituent files using JSON-LD with schema.org vocabulary. Key characteristics:

- **Flat `@graph` structure** -- all entities (dataset, files, people, organizations) appear as top-level objects in a flat `@graph` array, cross-referenced by `@id`.
- **Metadata File Descriptor** -- a `CreativeWork` entity with `@id: "ro-crate-metadata.json"` that points to the Root Data Entity via `about`.
- **Root Data Entity** -- a `Dataset` entity (typically `@id: "./"`) describing the crate as a whole.
- **Data Entities** -- `File` (alias for `MediaObject`) and `Dataset` entities representing files and folders.
- **Contextual Entities** -- `Person`, `Organization`, `Place`, etc. entities referenced from the data entities.

See the [RO-Crate 1.2 specification](https://www.researchobject.org/ro-crate/specification/1.2/introduction.html) and [quick reference](https://www.researchobject.org/ro-crate/quick-reference) for details.

## Property Mapping: adaProduct / CDIFcomplete to RO-Crate

Both profiles and RO-Crate use schema.org as their primary vocabulary, so many properties map directly. The table below shows how metadata from the ADA/CDIF profiles corresponds to RO-Crate Root Data Entity properties.

### Root Data Entity (Dataset)

| ADA / CDIF Property | RO-Crate Property | Notes |
|---|---|---|
| `@type: ["schema:Dataset", ...]` | `@type: "Dataset"` | ADA adds `"schema:Product"`; RO-Crate requires `Dataset` |
| `schema:name` | `name` | Direct mapping |
| `schema:description` | `description` | Direct mapping |
| `schema:dateModified` | `datePublished` | RO-Crate requires `datePublished` (MUST); ADA uses `dateModified`. Use `schema:datePublished` if present, fall back to `dateModified` |
| `schema:identifier` | `identifier` | ADA uses structured `PropertyValue`; RO-Crate recommends DOI URI string |
| `schema:license` | `license` | ADA stores as array of URI strings; RO-Crate expects `{"@id": "..."}` reference to a contextual entity |
| `schema:url` | `url` | Direct mapping (landing page) |
| `schema:keywords` | `keywords` | ADA allows mixed `DefinedTerm` objects and strings; RO-Crate expects strings or `DefinedTerm` references |
| `schema:creator` | `author` | ADA uses `schema:creator` with `@list`; RO-Crate uses `author` with entity references |
| `schema:contributor` | `contributor` | ADA wraps in `schema:Role`; RO-Crate uses flat entity references |
| `schema:funding` | `funder` / `funding` | ADA uses `MonetaryGrant` with nested `funder`; RO-Crate uses contextual entity references |
| `schema:publisher` / `schema:provider` | `publisher` | Direct mapping via entity reference |
| `schema:spatialCoverage` | `spatialCoverage` | Both use `schema:Place` with `schema:geo` |
| `schema:temporalCoverage` | `temporalCoverage` | Direct mapping (ISO 8601 interval string) |
| `schema:version` | `version` | Direct mapping |
| `schema:distribution` | `hasPart` | **Structural difference** -- see below |
| `schema:subjectOf` | (metadata descriptor) | ADA/CDIF meta-metadata maps to the RO-Crate Metadata File Descriptor entity |
| `dcterms:conformsTo` | `conformsTo` | Profile declarations move to Root Data Entity `conformsTo` |
| `prov:wasGeneratedBy` | -- | ADA-specific; can be included as additional schema.org/PROV-O properties |
| `schema:variableMeasured` | -- | CDIF data description; can be included as `variableMeasured` contextual entities |

### Data Entities (Files)

| ADA / CDIF Property | RO-Crate Property | Notes |
|---|---|---|
| `@type` (e.g., `["ada:image", "schema:ImageObject"]`) | `@type: "File"` | RO-Crate uses `File` (alias for `MediaObject`); additional types can be kept |
| `schema:name` | `name` | Filename within the archive |
| `schema:description` | `description` | Direct mapping |
| `schema:encodingFormat` | `encodingFormat` | ADA stores as array; RO-Crate expects single MIME string |
| `schema:size` | `contentSize` | ADA uses structured `QuantitativeValue`; RO-Crate expects byte count string |
| `spdx:checksum` | -- | No direct RO-Crate equivalent; preserve as additional property |
| `schema:additionalType` | `additionalType` | ADA component types can be preserved |
| `componentType` | -- | ADA-specific detail; can be preserved as additional property |

### Contextual Entities (People, Organizations)

| ADA / CDIF Property | RO-Crate Property | Notes |
|---|---|---|
| `schema:Person` with `schema:name`, `schema:identifier` | `Person` with `name`, ORCID `@id` | RO-Crate prefers ORCID as `@id` rather than nested identifier |
| `schema:Organization` with `schema:name` | `Organization` with `name`, ROR `@id` | RO-Crate prefers ROR identifier as `@id` |
| `schema:Place` | `Place` | ADA instruments/labs map to contextual entities |

## Key Structural Differences

### 1. Nested vs. Flat Graph

The most significant difference is the document structure:

- **ADA/CDIF metadata** uses nested JSON-LD -- persons, organizations, files, and distributions are embedded inline within the dataset object.
- **RO-Crate** requires a **flat `@graph` array** where every entity is a top-level object referenced by `@id`.

Example -- a creator in ADA metadata:
```json
{
  "schema:creator": {
    "@list": [{
      "@type": "schema:Person",
      "schema:name": "Analytica, Maria",
      "schema:identifier": "https://orcid.org/0000-0001-2345-6789"
    }]
  }
}
```

The same creator in RO-Crate:
```json
{
  "@id": "./",
  "@type": "Dataset",
  "author": [{"@id": "https://orcid.org/0000-0001-2345-6789"}]
}
```
```json
{
  "@id": "https://orcid.org/0000-0001-2345-6789",
  "@type": "Person",
  "name": "Analytica, Maria"
}
```

### 2. Distribution vs. hasPart

ADA/CDIF metadata wraps files inside a `schema:distribution` array, which contains an archive `DataDownload` object with nested `schema:hasPart` file items. RO-Crate puts files directly as top-level `File` entities in the `@graph`, referenced from the root `Dataset` via `hasPart`:

```json
{
  "@id": "./",
  "@type": "Dataset",
  "hasPart": [
    {"@id": "ALH84001_ADA_001.tif"},
    {"@id": "ALH84001_ADA_methods.pdf"}
  ]
}
```

### 3. Prefixed vs. Unprefixed Properties

ADA/CDIF metadata uses namespace-prefixed property names (e.g., `schema:name`, `schema:description`). RO-Crate uses unprefixed schema.org terms (e.g., `name`, `description`) resolved through its own `@context`.

### 4. Metadata File Descriptor

RO-Crate requires a special `CreativeWork` entity describing the metadata file itself. ADA/CDIF metadata has an analogous `schema:subjectOf` object that describes the metadata record. The translator maps this to the RO-Crate Metadata File Descriptor.

## Translator: ADA/CDIF Metadata to RO-Crate

### How the Translator Works

The translator reads a JSON-LD metadata document conforming to either the adaProduct or CDIFcomplete profile and produces a conformant `ro-crate-metadata.json`. The transformation has five stages:

#### Stage 1: Initialize the RO-Crate Shell

Create the base `@graph` with two required entities:

```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {"@id": "./"},
      "conformsTo": {"@id": "https://w3id.org/ro/crate/1.2"}
    },
    {
      "@id": "./",
      "@type": "Dataset"
    }
  ]
}
```

#### Stage 2: Map Root Dataset Properties

Copy dataset-level properties from the source metadata to the Root Data Entity, stripping `schema:` prefixes and restructuring values:

1. **Simple properties**: `schema:name` -> `name`, `schema:description` -> `description`, `schema:version` -> `version`, `schema:url` -> `url`
2. **Date**: Use `schema:datePublished` if present, otherwise `schema:dateModified` -> `datePublished`
3. **Identifier**: Extract DOI URI from the structured `PropertyValue` -> `identifier`
4. **License**: Convert URI string to `{"@id": "https://creativecommons.org/..."}` and create a contextual `CreativeWork` entity in the graph
5. **Keywords**: Flatten `DefinedTerm` objects to strings, or keep as contextual entity references
6. **Spatial/temporal coverage**: Map `schema:spatialCoverage` -> `spatialCoverage`, `schema:temporalCoverage` -> `temporalCoverage`
7. **Conformance**: Copy `dcterms:conformsTo` profile URIs to `conformsTo` on the Root Data Entity

#### Stage 3: Extract Contextual Entities (Flatten)

Walk through nested objects in the source metadata and extract each as a top-level `@graph` entity:

1. **Persons** (from `schema:creator`, `schema:contributor`):
   - Use ORCID as `@id` if available, otherwise mint a local `#person-N` id
   - Map `schema:name` -> `name`, `schema:affiliation` -> `affiliation` (as entity reference)
   - Add to Root Data Entity as `author` or `contributor` references

2. **Organizations** (from affiliations, funders, publishers):
   - Use ROR identifier as `@id` if available
   - Map `schema:name` -> `name`

3. **Funding** (from `schema:funding`):
   - Extract `MonetaryGrant` as contextual entity with `funder` reference
   - Add to Root Data Entity as `funding` reference

4. **Provenance** (ADA-specific `prov:wasGeneratedBy`):
   - Extract analysis events as `Action` entities
   - Extract instruments and laboratories as contextual entities
   - Extract samples as contextual entities
   - Preserve `prov:` properties as additional linked data

5. **Variables** (from `schema:variableMeasured`):
   - Extract each `PropertyValue`/`cdi:InstanceVariable` as a contextual entity
   - Reference from Root Data Entity via `variableMeasured`

#### Stage 4: Map Data Entities (Files)

Process the `schema:distribution` array to extract file entities:

1. **Archive distribution** (distribution with `schema:hasPart`):
   - Each `schema:hasPart` item becomes a top-level `File` entity in the graph
   - `@id` is the filename (relative path): `schema:name` -> `@id`
   - `@type` becomes `File` (plus any additional types from `schema:additionalType`)
   - `schema:encodingFormat` array -> `encodingFormat` (first element as string)
   - `schema:size` QuantitativeValue -> `contentSize` (value as string with "B" suffix)
   - `spdx:checksum` is preserved as an additional property
   - Collect file `@id` references for the Root Data Entity `hasPart`

2. **Single-file distribution** (no `schema:hasPart`):
   - The distribution itself becomes a `File` entity
   - `schema:contentUrl` -> `@id` (or use `schema:name` for local files)

3. **WebAPI distribution**:
   - Becomes a contextual `WebAPI` entity referenced from Root Data Entity
   - `schema:potentialAction` results are processed like single-file distributions

4. **CDIF data description** (CDIFcomplete-specific):
   - `cdi:hasPhysicalMapping` entries are preserved as additional properties on File entities
   - CSV-W tabular properties (`csvw:delimiter`, etc.) are preserved on File entities

#### Stage 5: Assemble and Validate

1. Collect all entities into the `@graph` array
2. Verify every `{"@id": "..."}` reference has a corresponding entity in the graph
3. Verify the Root Data Entity has `name`, `description`, `datePublished`, and `license`
4. Write `ro-crate-metadata.json`

### Example Transformation

Given this ADA metadata (abbreviated):

```json
{
  "@context": {"schema": "http://schema.org/", ...},
  "@id": "ex:adaProduct-example-001",
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:name": "ADA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example ADA product metadata...",
  "schema:dateModified": "2026-01-15",
  "schema:license": ["https://creativecommons.org/licenses/by/4.0/"],
  "schema:creator": {
    "@list": [{
      "@type": "schema:Person",
      "schema:name": "Analytica, Maria",
      "schema:identifier": "https://orcid.org/0000-0001-2345-6789"
    }]
  },
  "schema:distribution": [{
    "@type": ["schema:DataDownload"],
    "schema:additionalType": ["RO-CRATE"],
    "schema:hasPart": [
      {
        "@type": ["ada:image", "schema:ImageObject"],
        "schema:name": "ALH84001_ADA_001.tif",
        "schema:encodingFormat": ["image/tiff"],
        "schema:size": {"@type": "schema:QuantitativeValue", "schema:value": 10485760, "schema:unitText": "byte"}
      },
      {
        "@type": ["ada:document", "schema:DigitalDocument"],
        "schema:name": "ALH84001_ADA_methods.pdf",
        "schema:encodingFormat": ["application/pdf"]
      }
    ]
  }]
}
```

The translator produces:

```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {"@id": "./"},
      "conformsTo": {"@id": "https://w3id.org/ro/crate/1.2"}
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "ADA Analysis of Meteorite ALH 84001 Fragment",
      "description": "Example ADA product metadata...",
      "datePublished": "2026-01-15",
      "license": {"@id": "https://creativecommons.org/licenses/by/4.0/"},
      "identifier": "https://doi.org/10.99999/adaproduct-example-001",
      "author": [{"@id": "https://orcid.org/0000-0001-2345-6789"}],
      "conformsTo": [
        {"@id": "https://w3id.org/cdif/profiles/discovery"},
        {"@id": "https://ada.astromat.org/profiles/adaProduct"}
      ],
      "hasPart": [
        {"@id": "ALH84001_ADA_001.tif"},
        {"@id": "ALH84001_ADA_methods.pdf"}
      ]
    },
    {
      "@id": "https://orcid.org/0000-0001-2345-6789",
      "@type": "Person",
      "name": "Analytica, Maria"
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "name": "Creative Commons Attribution 4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
      "@id": "ALH84001_ADA_001.tif",
      "@type": ["File", "ImageObject"],
      "name": "ALH84001_ADA_001.tif",
      "encodingFormat": "image/tiff",
      "contentSize": "10485760"
    },
    {
      "@id": "ALH84001_ADA_methods.pdf",
      "@type": ["File", "DigitalDocument"],
      "name": "ALH84001_ADA_methods.pdf",
      "encodingFormat": "application/pdf"
    }
  ]
}
```

### What is Preserved, What is Lost

| Category | Preserved in RO-Crate | Notes |
|---|---|---|
| Dataset identity and description | name, description, datePublished, license, identifier, url, version, keywords | Core overlap between schemas |
| People and organizations | author, contributor, publisher with ORCID/ROR identifiers | Flattened from nested to entity references |
| Spatial and temporal coverage | spatialCoverage, temporalCoverage | Direct mapping |
| Funding | funding with funder references | MonetaryGrant as contextual entity |
| File inventory | hasPart with File entities, MIME types, sizes | Restructured from distribution/hasPart to flat graph |
| Profile conformance | conformsTo | Moved from subjectOf to Root Data Entity |
| ADA analysis provenance | Additional PROV-O properties | Preserved but not part of core RO-Crate spec |
| ADA instrument/lab details | Contextual entities | Preserved as additional linked data entities |
| CDIF variable descriptions | variableMeasured entities | Preserved with DDI-CDI typing |
| CDIF physical mappings | Additional properties on File entities | Preserved but not standard RO-Crate |
| ADA componentType | -- | Domain-specific; not representable in core RO-Crate |
| CSV-W tabular properties | Additional properties on File entities | Preserved; CSV-W is in RO-Crate context |

## References

- [RO-Crate 1.2 Specification](https://www.researchobject.org/ro-crate/specification/1.2/introduction.html)
- [RO-Crate Quick Reference](https://www.researchobject.org/ro-crate/quick-reference)
- [RO-Crate Root Data Entity](https://www.researchobject.org/ro-crate/specification/1.2/root-data-entity.html)
- [RO-Crate Data Entities](https://www.researchobject.org/ro-crate/specification/1.2/data-entities)
- [RO-Crate Metadata](https://www.researchobject.org/ro-crate/specification/1.1/metadata.html)
- [RO-Crate JSON-LD](https://www.researchobject.org/ro-crate/specification/1.1/appendix/jsonld.html)
- [CDIF Book: Schema.org Implementation](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html)
