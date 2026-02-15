
# ADA QRIS Profile (Schema)

`cdif.bbr.metadata.profiles.adaQRIS` *v0.1*

Technique-specific profile for Quantitative Reflectance Imaging Spectroscopy (QRIS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA QRIS Profile

Technique-specific metadata profile for Quantitative Reflectance Imaging Spectroscopy (QRIS) products in the Astromat Data Archive. Quantitative reflectance imaging spectroscopy.

## Product Types
- `ada:QRISCalibratedCollection`
- `ada:QRISRawCollection`
- `ada:QRISCalibrationFile`

## Valid Component Types
- `ada:QRISCalibratedCollection`
- `ada:QRISRawCollection`
- `ada:QRISCalibrationFile`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailQRIS`

## Examples

### QRIS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:QRISCalibratedCollection", "ada:DataDeliveryPackage"],
  "schema:name": "QRIS Analysis of Sample",
  "schema:description": "Quantitative Reflectance Imaging Spectroscopy (QRIS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaQRIS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:QRISCalibratedCollection",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "QRIS Analysis of Sample",
  "schema:description": "Quantitative Reflectance Imaging Spectroscopy (QRIS) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:QRISCalibratedCollection" ;
    ns1:description "Quantitative Reflectance Imaging Spectroscopy (QRIS) data" ;
    ns1:name "QRIS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA QRIS Product Profile
description: Technique-specific profile for Quantitative Reflectance Imaging Spectroscopy
  (QRIS) products. Extends the base ADA product profile with constraints on valid
  QRIS component types and detailQRIS requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a QRIS product type identifier.
      contains:
        enum:
        - ada:QRISCalibratedCollection
        - ada:QRISRawCollection
        - ada:QRISCalibrationFile
        - Quantitative Reflectance Imaging System
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:QRISCalibratedCollection
                    - ada:QRISRawCollection
                    - ada:QRISCalibrationFile
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaQRIS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaQRIS/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "https://schema.org",
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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaQRIS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaQRIS`

