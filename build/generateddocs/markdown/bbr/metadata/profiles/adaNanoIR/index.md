
# ADA NanoIR Profile (Schema)

`cdif.bbr.metadata.profiles.adaNanoIR` *v0.1*

Technique-specific profile for Nano-Infrared Spectroscopy (NanoIR) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA NanoIR Profile

Technique-specific metadata profile for Nano-Infrared Spectroscopy (NanoIR) products in the Astromat Data Archive. Nano-infrared spectroscopy and photothermal imaging.

## Product Types
- `ada:NanoIRBackground`
- `ada:NanoIRMap`
- `ada:NanoIRMapCollection`
- `ada:NanoIRPointCollection`

## Valid Component Types
- `ada:NanoIRBackground`
- `ada:NanoIRMap`
- `ada:NanoIRMapCollection`
- `ada:NanoIRPointCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailNanoIR`

## Examples

### NanoIR Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:NanoIRBackground", "ada:DataDeliveryPackage"],
  "schema:name": "NanoIR Analysis of Sample",
  "schema:description": "Nano-Infrared Spectroscopy (NanoIR) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA NanoIR Product Profile
description: Technique-specific profile for Nano-Infrared Spectroscopy (NanoIR) products.
  Extends the base ADA product profile with constraints on valid NanoIR component
  types and detailNanoIR requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a NanoIR product type identifier.
      contains:
        enum:
        - ada:NanoIRBackground
        - ada:NanoIRMap
        - ada:NanoIRMapCollection
        - ada:NanoIRPointCollection
        - Nanoscale Infrared Mapping
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:NanoIRBackground
                    - ada:NanoIRMap
                    - ada:NanoIRMapCollection
                    - ada:NanoIRPointCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaNanoIR/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaNanoIR/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaNanoIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaNanoIR`

