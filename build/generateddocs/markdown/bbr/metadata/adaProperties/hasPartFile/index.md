
# Has Part File Type (Schema)

`cdif.bbr.metadata.adaProperties.hasPartFile` *v0.1*

Files within archive distribution, extends files type

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Has Part File Type

Describes files within an archive distribution (e.g., files inside a zip archive). Reuses the files type schema for describing individual files within a `schema:hasPart` array of a `schema:DataDownload` distribution.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Has Part File Type
description: Files within an archive package (hasPart). Uses CDIF 2026 distribution
  patterns with DDI-CDI types. The @type must NOT contain schema:DataDownload (distinguishing
  hasPart files from top-level distribution files). File-type details are merged via
  allOf rather than nested in fileDetail.
allOf:
- type: object
  properties:
    '@id':
      type: string
    '@type':
      type: array
      items:
        type: string
      not:
        contains:
          const: schema:DataDownload
      minItems: 1
    schema:additionalType:
      type: array
      description: The dataComponentType or supDocType
      items:
        type: string
    schema:name:
      type: string
      description: String name of file, must be unique within the containing package
    schema:description:
      type: string
    spdx:checksum:
      type: object
      properties:
        spdx:algorithm:
          type: string
        spdx:checksumValue:
          type: string
    schema:size:
      type: object
      properties:
        '@type':
          const: schema:QuantitativeValue
        schema:value:
          type: integer
        schema:unitText:
          type: string
          default: byte
    schema:encodingFormat:
      type: array
      items:
        type: string
- anyOf:
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/image/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/imageMap/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/tabularData/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/collection/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/dataCube/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/document/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.yaml
  - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/otherFile/schema.yaml
  - type: object
    properties:
      '@type':
        const:
        - Metadata
    required:
    - '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/hasPartFile`

