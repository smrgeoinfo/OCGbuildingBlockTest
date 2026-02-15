
# NanoIR Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailNanoIR` *v0.1*

Nano-IR spectroscopy collections with phase analysis

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoIR Instrument Detail

Nano-IR spectroscopy collections with phase analysis.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoIR Instrument Detail
description: Nano-IR spectroscopy collections with phase analysis
type: object
properties:
  '@type':
    anyOf:
    - const: ada:NanoIRBackground
  phaseAnalyzed:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoIR/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailNanoIR`

