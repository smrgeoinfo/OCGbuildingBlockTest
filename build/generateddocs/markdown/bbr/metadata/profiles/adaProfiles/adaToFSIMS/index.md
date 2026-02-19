
# ADA ToF-SIMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaProfiles.adaToFSIMS` *v0.1*

Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ToF-SIMS Profile

Technique-specific metadata profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products in the Astromat Data Archive. Time-of-flight secondary ion mass spectrometry surface analysis.

## Product Types
- `ada:TOFSIMSCollection`

## Valid Component Types
- `ada:TOFSIMSCollection`
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

## Examples

### ToF-SIMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["Time-of-flight secondary ion mass spectrometry (TOFSIMS)", "ada:DataDeliveryPackage"],
  "schema:name": "ToF-SIMS Analysis of Sample",
  "schema:description": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "ToF-SIMS Analysis of Sample",
  "schema:description": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Time-of-flight secondary ion mass spectrometry (TOFSIMS)",
        "ada:DataDeliveryPackage" ;
    schema1:description "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) data" ;
    schema1:name "ToF-SIMS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ToF-SIMS Product Profile
description: Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry
  (ToF-SIMS) products. Extends the base ADA product profile with constraints on valid
  ToF-SIMS component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ToF-SIMS product type identifier.
      contains:
        enum:
        - Time-of-flight secondary ion mass spectrometry (TOFSIMS)
        - Time-of-Flight Secondary Ion Mass Spectrometry
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
                      - ada:TOFSIMSCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaToFSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaToFSIMS`

