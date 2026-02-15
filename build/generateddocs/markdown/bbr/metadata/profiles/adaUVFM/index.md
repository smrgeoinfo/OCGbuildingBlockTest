
# ADA UVFM Profile (Schema)

`cdif.bbr.metadata.profiles.adaUVFM` *v0.1*

Technique-specific profile for Ultraviolet Fluorescence Microscopy (UVFM) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA UVFM Profile

Technique-specific metadata profile for Ultraviolet Fluorescence Microscopy (UVFM) products in the Astromat Data Archive. Ultraviolet fluorescence microscopy imaging.

## Product Types
- `ada:UVFMImage`
- `ada:UVFMImageCollection`

## Valid Component Types
- `ada:UVFMImage`
- `ada:UVFMImageCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### UVFM Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:UVFMImage", "ada:DataDeliveryPackage"],
  "schema:name": "UVFM Analysis of Sample",
  "schema:description": "Ultraviolet Fluorescence Microscopy (UVFM) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA UVFM Product Profile
description: Technique-specific profile for Ultraviolet Fluorescence Microscopy (UVFM)
  products. Extends the base ADA product profile with constraints on valid UVFM component
  types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a UVFM product type identifier.
      contains:
        enum:
        - ada:UVFMImage
        - ada:UVFMImageCollection
        - UV Fluorescence Microscopy
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:UVFMImage
                    - ada:UVFMImageCollection
                    - ada:analysisLocation
                    - ada:methodDescription
                    - ada:instrumentMetadata
                    - ada:calibrationFile
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  nxs: http://purl.org/nexusformat/definitions/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaUVFM/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaUVFM/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaUVFM/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaUVFM`

