
# Supplemental Document Image Type (Schema)

`cdif.bbr.metadata.adaProperties.supDocImage` *v0.1*

Supplemental document images including analysis locations and context photos

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Supplemental Document Image Type

Describes supplemental document images such as analysis location images, annotated products, context photography, areas of interest, instrument metadata images, supplemental basemaps, plots, quick-look images, reports, and visual images.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Supplemental Document Image Type
description: Supplemental document images including analysis location images, annotated
  products, context photography, and other supplemental visual materials.
type: object
properties:
  '@type':
    const:
    - ada:image
    - schema:DigitalDocument
    description: GeneralType for supplemental document images
  componentType:
    type: object
    properties:
      '@type':
        enum:
        - ada:analysisLocation
        - ada:annotatedProduct
        - ada:contextPhotography
        - ada:areaOfInterest
        - ada:instrumentMetadata
        - ada:supplementalBasemap
        - ada:other
        - ada:plot
        - ada:quickLook
        - ada:report
        - ada:visImage
    required:
    - '@type'
  numPixelsX:
    type: integer
  numPixelsY:
    type: integer
  _original_name:
    type: string
required:
- '@type'
- componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/supDocImage/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/supDocImage/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/supDocImage`

