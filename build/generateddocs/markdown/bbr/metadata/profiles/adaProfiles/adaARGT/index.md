
# ADA ARGT Profile (Schema)

`cdif.bbr.metadata.profiles.adaProfiles.adaARGT` *v0.1*

Technique-specific profile for Argon Geochronology and Thermochronology (ARGT) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ARGT Profile

Technique-specific metadata profile for Argon Geochronology and Thermochronology (ARGT) products in the Astromat Data Archive. Argon geochronology and thermochronology dating analysis.

## Product Types
- `ada:ARGTDocument`
- `ada:ARGTCollection`

## Valid Component Types
- `ada:ARGTDocument`
- `ada:ARGTCollection`
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
`detailARGT`

## Examples

### ARGT Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["⁴⁰Ar/³⁹Ar Geochronology and Thermochronology (ARGT)", "ada:DataDeliveryPackage"],
  "schema:name": "ARGT Analysis of Sample",
  "schema:description": "Argon Geochronology and Thermochronology (ARGT) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaARGT/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "\u2074\u2070Ar/\u00b3\u2079Ar Geochronology and Thermochronology (ARGT)",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "ARGT Analysis of Sample",
  "schema:description": "Argon Geochronology and Thermochronology (ARGT) data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "ada:DataDeliveryPackage",
        "⁴⁰Ar/³⁹Ar Geochronology and Thermochronology (ARGT)" ;
    schema1:description "Argon Geochronology and Thermochronology (ARGT) data" ;
    schema1:name "ARGT Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ARGT Product Profile
description: Technique-specific profile for Argon Geochronology and Thermochronology
  (ARGT) products. Extends the base ADA product profile with constraints on valid
  ARGT component types and detailARGT requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ARGT product type identifier.
      contains:
        enum:
        - "\u2074\u2070Ar/\xB3\u2079Ar Geochronology and Thermochronology (ARGT)"
        - 40Ar/39Ar geochronology and thermochronology
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
                      - ada:ARGTDocument
                      - ada:ARGTCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaARGT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaARGT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaARGT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaARGT`

