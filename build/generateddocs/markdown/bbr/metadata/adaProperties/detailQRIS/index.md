
# QRIS Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailQRIS` *v0.1*

QRIS (Raman) with calibration and illumination parameters

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# QRIS Instrument Detail

QRIS (Raman) with calibration and illumination parameters. (Extension type, not in v3 source schema.)

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: QRIS Instrument Detail
description: QRIS (Raman) with calibration and illumination parameters. (Extension
  type, not in v3 source schema.)
type: object
properties:
  '@type':
    anyOf:
    - const: ada:QRISCalibrated
    - const: ada:QRISRaw
  calibrationFile:
    type: string
  pipelineVersion:
    type: string
  focalLength:
    type: integer
  illuminationColor:
    type: array
    minItems: 0
    items:
      type: string
  illuminationLevel:
    type: integer
  exposureTime:
    type: integer
  target:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailQRIS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailQRIS/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailQRIS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailQRIS`

