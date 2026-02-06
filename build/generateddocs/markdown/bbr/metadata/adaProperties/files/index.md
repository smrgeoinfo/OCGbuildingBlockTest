
# Files Type (Schema)

`cdif.bbr.metadata.adaProperties.files` *v0.1*

DataDownload with checksum, size, encoding format, and file detail

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Files Type

Describes properties for any file in an ADA product. Includes file metadata (name, description, checksum, size, encoding format), file detail classification (image, imageMap, tabularData, collection, dataCube, document, supDocImage, otherFile, or Metadata), and inter-file relationships via `schema:relatedLink`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Files Type
description: Properties for any file in an ADA product distribution. The @type must
  include schema:DataDownload per CDIF 2026 patterns. GeneralType provides info based
  on broad categories of file format (tabular, image, dataCube, document).
type: object
properties:
  '@id':
    type: string
  '@type':
    type: array
    items:
      type: string
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
    description: A string value calculated from the content of the resource representation,
      used to test if content has been modified.
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
    description: MIME type with extension; should indicate the serialization scheme
      in sufficient detail that machine can know how to parse.
  resultTarget:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
  fileDetail:
    anyOf:
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
  schema:relatedLink:
    type: array
    description: 'Links between files in the product. Use schema:name for path to
      target in product, or use #id JSON-LD links.'
    items:
      type: object
      properties:
        '@type':
          type: string
          const: schema:LinkRole
        schema:linkRelationship:
          type: string
        schema:target:
          type: object
          properties:
            '@type':
              type: string
              const: schema:EntryPoint
            schema:encodingFormat:
              type: string
            schema:name:
              type: string
            schema:url:
              type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/files/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/files/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/files/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/files`

