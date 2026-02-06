
# SLS Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailSLS` *v0.1*

Structured Light Scanning shape models and partial scans

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SLS Instrument Detail

Structured Light Scanning shape models and partial scans.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SLS Instrument Detail
description: Structured Light Scanning shape models and partial scans
type: object
properties:
  '@type':
    anyOf:
    - const: ada:SLSShapeModel
    - const: ada:SLSPartialScan
  countScans:
    type: integer
  facets:
    type: integer
  unitsOfMeasurement:
    type: string
  version:
    type: integer
  vertices:
    type: integer
  watertight:
    type: boolean
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailSLS/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailSLS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailSLS`

