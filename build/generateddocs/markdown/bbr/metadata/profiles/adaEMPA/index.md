
# ADA EMPA Profile (Schema)

`cdif.bbr.metadata.profiles.adaEMPA` *v0.1*

Technique-specific profile for Electron Microprobe Analysis (EMPA) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA EMPA Profile

Technique-specific metadata profile for Electron Microprobe Analysis (EMPA) products in the Astromat Data Archive. EMPA uses focused electron beams to determine chemical composition of small volumes of solid materials through characteristic X-ray emission.

## Product Types
- **EMPA Image** - Backscattered electron or secondary electron images
- **EMPA Collection** - Sets of EMPA images or maps
- **EMPA QEA** - Quantitative elemental analysis tabular data
- **EMPA SPC** - Spectral data from electron microprobe

## Valid Component Types
- `ada:EMPAImageMap` - Image maps with spectrometer and signal detail (empa_detail)
- `ada:EMPAImage` - Individual EMPA images
- `ada:EMPAQEATabular` - Quantitative elemental analysis tables (empa_detail)
- `ada:EMPAImageCollection` - Collections of EMPA images
- `ada:analysisLocation` - Supplemental analysis location images
- `ada:supplementaryImage` - Supplementary visual materials
- `ada:calibrationFile` - Calibration documents
- `ada:methodDescription` - Method description documents
- `ada:instrumentMetadata` - Instrument metadata documents

## Detail Type
`empa_detail` with properties: `spectrometersUsed`, `signalUsed`

## Examples

### EMPA Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:EMPAImage", "ada:DataDeliveryPackage"],
  "schema:name": "EMPA Analysis of Meteorite Sample",
  "schema:description": "Electron microprobe analysis data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA EMPA Product Profile
description: Technique-specific profile for Electron Microprobe Analysis (EMPA) products.
  Extends the base ADA product profile with constraints on valid EMPA component types
  and empa_detail requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include an EMPA product type identifier.
      contains:
        enum:
        - ada:EMPAImage
        - ada:EMPACollection
        - ada:EMPAQEA
        - ada:EMPAESPC
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:EMPAImageMap
                    - ada:EMPAImage
                    - ada:EMPAQEATabular
                    - ada:EMPAImageCollection
                    - ada:analysisLocation
                    - ada:supplementaryImage
                    - ada:calibrationFile
                    - ada:methodDescription
                    - ada:instrumentMetadata
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaEMPA/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaEMPA/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaEMPA`

