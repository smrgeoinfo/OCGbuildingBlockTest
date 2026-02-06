
# NanoSIMS Instrument Detail (Schema)

`cdif.bbr.metadata.adaProperties.detailNanoSIMS` *v0.1*

Nano Secondary Ion Mass Spectrometry with isotope tracking

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoSIMS Instrument Detail

Nano Secondary Ion Mass Spectrometry with isotope tracking.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoSIMS Instrument Detail
description: Nano Secondary Ion Mass Spectrometry with isotope tracking
type: object
properties:
  '@type':
    type: string
    enum:
    - ada:NanoSIMSCollection
    - ada:NanoSIMSImageCollection
    - ada:NanoSIMSTabular
    - ada:NanoSIMSMap
  phaseAnalyzed:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
  isotopeAnalyzed:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/stringArray/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/detailNanoSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/detailNanoSIMS`

