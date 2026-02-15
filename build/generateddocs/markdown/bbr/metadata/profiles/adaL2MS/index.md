
# ADA L2MS Profile (Schema)

`cdif.bbr.metadata.profiles.adaL2MS` *v0.1*

Technique-specific profile for Two-Step Laser Mass Spectrometry (L2MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA L2MS Profile

Technique-specific metadata profile for Two-Step Laser Mass Spectrometry (L2MS) products in the Astromat Data Archive. Two-step laser desorption/ionization mass spectrometry.

## Product Types
- `ada:L2MSCube`
- `ada:L2MSOverviewImage`

## Valid Component Types
- `ada:L2MSCube`
- `ada:L2MSOverviewImage`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailL2MS`

## Examples

### L2MS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:L2MSCube", "ada:DataDeliveryPackage"],
  "schema:name": "L2MS Analysis of Sample",
  "schema:description": "Two-Step Laser Mass Spectrometry (L2MS) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA L2MS Product Profile
description: Technique-specific profile for Two-Step Laser Mass Spectrometry (L2MS)
  products. Extends the base ADA product profile with constraints on valid L2MS component
  types and detailL2MS requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a L2MS product type identifier.
      contains:
        enum:
        - ada:L2MSCube
        - ada:L2MSOverviewImage
        - Microprobe Two-Step Laser Mass Spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:L2MSCube
                    - ada:L2MSOverviewImage
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaL2MS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaL2MS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaL2MS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaL2MS`

