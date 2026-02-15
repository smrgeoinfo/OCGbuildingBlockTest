
# PSFD Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailPSFD` *v0.1*

Point Spread Function Data with image names and conditions

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# PSFD Instrument Detail

Point Spread Function Data with image names and conditions.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PSFD Instrument Detail
description: Point Spread Function Data with image names and conditions
type: object
properties:
  '@type':
    const: ada:PSFDTabular
  imageName:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
  imageViewingConditions:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailPSFD/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailPSFD/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailPSFD/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/adaProperties/detailPSFD`

