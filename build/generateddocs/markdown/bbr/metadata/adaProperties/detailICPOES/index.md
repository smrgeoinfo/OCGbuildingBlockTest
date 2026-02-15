
# ICP-OES Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailICPOES` *v0.1*

Inductively Coupled Plasma Optical Emission Spectrometry detail properties

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ICP-OES Instrument Detail

Inductively Coupled Plasma Optical Emission Spectrometry. (Extension type, not in v3 source schema.)

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ICP-OES Instrument Detail
description: Inductively Coupled Plasma Optical Emission Spectrometry. (Extension
  type, not in v3 source schema.)
type: object
properties:
  '@type':
    anyOf:
    - const: ada:ICPOESIntermediateTabular
    - const: ada:ICPOESProcessedTabular
    - const: ada:ICPOESRawTabular
  mass:
    type: string
  dissolutionFactor:
    type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailICPOES/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailICPOES/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/adaProperties/detailICPOES/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/adaProperties/detailICPOES`

