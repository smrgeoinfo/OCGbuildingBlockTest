
# DSC Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailDSC` *v0.1*

Differential Scanning Calorimetry heat tabular data

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# DSC Instrument Detail

Differential Scanning Calorimetry heat tabular data.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DSC Instrument Detail
description: Differential Scanning Calorimetry heat tabular data
type: object
properties:
  '@type':
    const: ada:DSCHeatTabular
  analysisType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailDSC/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailDSC/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailDSC/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailDSC`

