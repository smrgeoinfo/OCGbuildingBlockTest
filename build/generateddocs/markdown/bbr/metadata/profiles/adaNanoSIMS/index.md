
# ADA NanoSIMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaNanoSIMS` *v0.1*

Technique-specific profile for Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA NanoSIMS Profile

Technique-specific metadata profile for Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) products in the Astromat Data Archive. Nanoscale secondary ion mass spectrometry imaging and analysis.

## Product Types
- `ada:NanoSIMSCollection`
- `ada:NanoSIMSImageCollection`
- `ada:NanoSIMSTabular`
- `ada:NanoSIMSMap`
- `ada:NanoSIMSImage`

## Valid Component Types
- `ada:NanoSIMSCollection`
- `ada:NanoSIMSImageCollection`
- `ada:NanoSIMSTabular`
- `ada:NanoSIMSMap`
- `ada:NanoSIMSImage`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailNanoSIMS`

## Examples

### NanoSIMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:NanoSIMSCollection", "ada:DataDeliveryPackage"],
  "schema:name": "NanoSIMS Analysis of Sample",
  "schema:description": "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA NanoSIMS Product Profile
description: Technique-specific profile for Nanoscale Secondary Ion Mass Spectrometry
  (NanoSIMS) products. Extends the base ADA product profile with constraints on valid
  NanoSIMS component types and detailNanoSIMS requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a NanoSIMS product type identifier.
      contains:
        enum:
        - ada:NanoSIMSCollection
        - ada:NanoSIMSImageCollection
        - ada:NanoSIMSTabular
        - ada:NanoSIMSMap
        - ada:NanoSIMSImage
        - Nanoscale secondary ion mass spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:NanoSIMSCollection
                    - ada:NanoSIMSImageCollection
                    - ada:NanoSIMSTabular
                    - ada:NanoSIMSMap
                    - ada:NanoSIMSImage
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaNanoSIMS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaNanoSIMS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaNanoSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaNanoSIMS`

