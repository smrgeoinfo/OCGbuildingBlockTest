
# ADA ICP-OES Profile (Schema)

`cdif.bbr.metadata.profiles.adaICPOES` *v0.1*

Technique-specific profile for Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ICP-OES Profile

Technique-specific metadata profile for Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) products in the Astromat Data Archive. Inductively coupled plasma optical emission spectrometry analysis.

## Product Types
- `ada:ICPOESIntermediateTabular`
- `ada:ICPOESProcessedTabular`
- `ada:ICPOESRawTabular`

## Valid Component Types
- `ada:ICPOESIntermediateTabular`
- `ada:ICPOESProcessedTabular`
- `ada:ICPOESRawTabular`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailICPOES`

## Examples

### ICP-OES Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:ICPOESIntermediateTabular", "ada:DataDeliveryPackage"],
  "schema:name": "ICP-OES Analysis of Sample",
  "schema:description": "Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPOES/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:ICPOESIntermediateTabular",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "ICP-OES Analysis of Sample",
  "schema:description": "Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:ICPOESIntermediateTabular" ;
    ns1:description "Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) data" ;
    ns1:name "ICP-OES Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ICP-OES Product Profile
description: Technique-specific profile for Inductively Coupled Plasma Optical Emission
  Spectrometry (ICP-OES) products. Extends the base ADA product profile with constraints
  on valid ICP-OES component types and detailICPOES requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ICP-OES product type identifier.
      contains:
        enum:
        - ada:ICPOESIntermediateTabular
        - ada:ICPOESProcessedTabular
        - ada:ICPOESRawTabular
        - Inductively coupled plasma - optical emission spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:ICPOESIntermediateTabular
                    - ada:ICPOESProcessedTabular
                    - ada:ICPOESRawTabular
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPOES/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPOES/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPOES/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaICPOES`

