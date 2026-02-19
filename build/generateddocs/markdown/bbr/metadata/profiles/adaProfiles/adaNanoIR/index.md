
# ADA NanoIR Profile (Schema)

`cdif.bbr.metadata.profiles.adaProfiles.adaNanoIR` *v0.1*

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
- `ada:annotatedImage`
- `ada:areaOfInterest`
- `ada:basemap`
- `ada:calibrationFile`
- `ada:code`
- `ada:contextPhotography`
- `ada:contextVideo`
- `ada:inputFile`
- `ada:instrumentMetadata`
- `ada:logFile`
- `ada:methodDescription`
- `ada:other`
- `ada:plot`
- `ada:processingMethod`
- `ada:quickLook`
- `ada:report`
- `ada:samplePreparation`
- `ada:shapefile`
- `ada:supplementalBasemap`
- `ada:supplementaryImage`
- `ada:worldFile`

## Detail Type
`detailNanoIR`

## Examples

### NanoIR Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["Nanoscale Infrared Mapping (NanoIR) Background", "ada:DataDeliveryPackage"],
  "schema:name": "NanoIR Analysis of Sample",
  "schema:description": "Nano-Infrared Spectroscopy (NanoIR) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoIR/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "Nanoscale Infrared Mapping (NanoIR) Background",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "NanoIR Analysis of Sample",
  "schema:description": "Nano-Infrared Spectroscopy (NanoIR) data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Nanoscale Infrared Mapping (NanoIR) Background",
        "ada:DataDeliveryPackage" ;
    schema1:description "Nano-Infrared Spectroscopy (NanoIR) data" ;
    schema1:name "NanoIR Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA NanoIR Product Profile
description: Technique-specific profile for Nano-Infrared Spectroscopy (NanoIR) products.
  Extends the base ADA product profile with constraints on valid NanoIR component
  types and detailNanoIR requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a NanoIR product type identifier.
      contains:
        enum:
        - Nanoscale Infrared Mapping (NanoIR) Background
        - Nanoscale Infrared Mapping (NanoIR) MapCollection
        - Nanoscale Infrared Mapping (NanoIR) Point Data
        - Nanoscale Infrared Mapping
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                componentType:
                  properties:
                    '@type':
                      enum:
                      - ada:NanoIRBackground
                      - ada:NanoIRMap
                      - ada:NanoIRMapCollection
                      - ada:NanoIRPointCollection
                      - ada:analysisLocation
                      - ada:annotatedImage
                      - ada:areaOfInterest
                      - ada:basemap
                      - ada:calibrationFile
                      - ada:code
                      - ada:contextPhotography
                      - ada:contextVideo
                      - ada:inputFile
                      - ada:instrumentMetadata
                      - ada:logFile
                      - ada:methodDescription
                      - ada:other
                      - ada:plot
                      - ada:processingMethod
                      - ada:quickLook
                      - ada:report
                      - ada:samplePreparation
                      - ada:shapefile
                      - ada:supplementalBasemap
                      - ada:supplementaryImage
                      - ada:worldFile
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoIR/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoIR/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaNanoIR`

