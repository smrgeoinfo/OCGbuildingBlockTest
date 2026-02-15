
# ADA FTICR-MS Profile (Schema)

`cdif.bbr.metadata.profiles.adaFTICRMS` *v0.1*

Technique-specific profile for Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA FTICR-MS Profile

Technique-specific metadata profile for Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) products in the Astromat Data Archive. Fourier transform ion cyclotron resonance mass spectrometry.

## Product Types
- `ada:FTICRMSTabular`
- `ada:FTICRMSCube`

## Valid Component Types
- `ada:FTICRMSTabular`
- `ada:FTICRMSCube`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### FTICR-MS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:FTICRMSTabular", "ada:DataDeliveryPackage"],
  "schema:name": "FTICR-MS Analysis of Sample",
  "schema:description": "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaFTICRMS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:FTICRMSTabular",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "FTICR-MS Analysis of Sample",
  "schema:description": "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:FTICRMSTabular" ;
    ns1:description "Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) data" ;
    ns1:name "FTICR-MS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA FTICR-MS Product Profile
description: Technique-specific profile for Fourier Transform Ion Cyclotron Resonance
  Mass Spectrometry (FTICR-MS) products. Extends the base ADA product profile with
  constraints on valid FTICR-MS component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a FTICR-MS product type identifier.
      contains:
        enum:
        - ada:FTICRMSTabular
        - ada:FTICRMSCube
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:FTICRMSTabular
                    - ada:FTICRMSCube
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaFTICRMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaFTICRMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaFTICRMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaFTICRMS`

