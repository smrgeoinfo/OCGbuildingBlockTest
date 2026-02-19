
# ADA NanoSIMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaProfiles.adaNanoSIMS` *v0.1*

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
`detailNanoSIMS`

## Examples

### NanoSIMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw", "ada:DataDeliveryPackage"],
  "schema:name": "NanoSIMS Analysis of Sample",
  "schema:description": "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoSIMS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "NanoSIMS Analysis of Sample",
  "schema:description": "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw",
        "ada:DataDeliveryPackage" ;
    schema1:description "Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) data" ;
    schema1:name "NanoSIMS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA NanoSIMS Product Profile
description: Technique-specific profile for Nanoscale Secondary Ion Mass Spectrometry
  (NanoSIMS) products. Extends the base ADA product profile with constraints on valid
  NanoSIMS component types and detailNanoSIMS requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a NanoSIMS product type identifier.
      contains:
        enum:
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Image
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Tabular
        - Nanoscale secondary ion mass spectrometry
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
                      - ada:NanoSIMSCollection
                      - ada:NanoSIMSImageCollection
                      - ada:NanoSIMSTabular
                      - ada:NanoSIMSMap
                      - ada:NanoSIMSImage
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoSIMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoSIMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaNanoSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaNanoSIMS`

