
# ADA LIT Profile (Schema)

`cdif.bbr.metadata.profiles.adaProfiles.adaLIT` *v0.1*

Technique-specific profile for Lock-In Thermography (LIT) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA LIT Profile

Technique-specific metadata profile for Lock-In Thermography (LIT) products in the Astromat Data Archive. Lock-in thermography imaging and data collection.

## Product Types
- `ada:LITImage`
- `ada:LIT2DDataCollection`
- `ada:LITPolarDataCollection`

## Valid Component Types
- `ada:LITImage`
- `ada:LIT2DDataCollection`
- `ada:LITPolarDataCollection`
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

### LIT Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["Lock-In Thermography (LIT) image", "ada:DataDeliveryPackage"],
  "schema:name": "LIT Analysis of Sample",
  "schema:description": "Lock-In Thermography (LIT) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaLIT/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "Lock-In Thermography (LIT) image",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "LIT Analysis of Sample",
  "schema:description": "Lock-In Thermography (LIT) data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Lock-In Thermography (LIT) image",
        "ada:DataDeliveryPackage" ;
    schema1:description "Lock-In Thermography (LIT) data" ;
    schema1:name "LIT Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA LIT Product Profile
description: Technique-specific profile for Lock-In Thermography (LIT) products. Extends
  the base ADA product profile with constraints on valid LIT component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a LIT product type identifier.
      contains:
        enum:
        - Lock-In Thermography (LIT) image
        - Lock-In Thermography (LIT) Collection
        - Lock-In Thermography
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
                      - ada:LITImage
                      - ada:LIT2DDataCollection
                      - ada:LITPolarDataCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaLIT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaLIT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaLIT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaLIT`

