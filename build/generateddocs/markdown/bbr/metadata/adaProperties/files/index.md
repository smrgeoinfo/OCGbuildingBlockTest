
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
description: Properties for any file in an ADA product distribution. GeneralType provides
  info based on broad categories of file format (tabular, image, dataCube, document).
  Type constraints (e.g. DataDownload) are applied at the composition level in profiles.
allOf:
- type: object
  properties:
    '@id':
      type: string
    '@type':
      type: array
      items:
        type: string
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
      $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/stringArray/stringArraySchema.json
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
- anyOf:
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/image/imageSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/imageMap/imageMapSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/tabularData/tabularDataSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/collection/collectionSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/dataCube/dataCubeSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/document/documentSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/supDocImage/supDocImageSchema.json
  - $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/adaProperties/otherFile/otherFileSchema.json
  - type: object
    properties:
      '@type':
        const:
        - Metadata
    required:
    - '@type'
  - type: object
    description: DataDownload distribution (archive or direct download without specific
      file type)
    properties:
      '@type':
        type: array
        contains:
          const: schema:DataDownload
    required:
    - '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "spdx": "http://spdx.org/rdf/terms#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/files/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/adaProperties/files`

