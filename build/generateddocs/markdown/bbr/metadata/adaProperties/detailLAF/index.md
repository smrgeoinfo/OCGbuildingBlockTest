
# LAF Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailLAF` *v0.1*

Laser Ablation Fluorescence processed/raw data detail properties

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# LAF Instrument Detail

Laser Ablation Fluorescence processed/raw data. elementAnalyzed goes in resultTarget.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LAF Instrument Detail
description: Laser Ablation Fluorescence processed/raw data. elementAnalyzed goes
  in resultTarget.
type: object
properties:
  '@type':
    anyOf:
    - const: ada:LAFProcessed
    - const: ada:LAFRaw
  elementAnalyzed:
    type: string
  sampleMassConsumed:
    type: string
  sampleType:
    type: string
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailLAF/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailLAF/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailLAF/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailLAF`

