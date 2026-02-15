
# ADA LC-MS Profile (Schema)

`cdif.bbr.metadata.profiles.adaLCMS` *v0.1*

Technique-specific profile for Liquid Chromatography Mass Spectrometry (LC-MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA LC-MS Profile

Technique-specific metadata profile for Liquid Chromatography Mass Spectrometry (LC-MS) products in the Astromat Data Archive. Liquid chromatography mass spectrometry analysis.

## Product Types
- `ada:LCMSCollection`
- `ada:LCMSMSCollection`

## Valid Component Types
- `ada:LCMSCollection`
- `ada:LCMSMSCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### LC-MS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:LCMSCollection", "ada:DataDeliveryPackage"],
  "schema:name": "LC-MS Analysis of Sample",
  "schema:description": "Liquid Chromatography Mass Spectrometry (LC-MS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLCMS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:LCMSCollection",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "LC-MS Analysis of Sample",
  "schema:description": "Liquid Chromatography Mass Spectrometry (LC-MS) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:LCMSCollection" ;
    ns1:description "Liquid Chromatography Mass Spectrometry (LC-MS) data" ;
    ns1:name "LC-MS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA LC-MS Product Profile
description: Technique-specific profile for Liquid Chromatography Mass Spectrometry
  (LC-MS) products. Extends the base ADA product profile with constraints on valid
  LC-MS component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a LC-MS product type identifier.
      contains:
        enum:
        - ada:LCMSCollection
        - ada:LCMSMSCollection
        - Liquid chromatography-mass spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:LCMSCollection
                    - ada:LCMSMSCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLCMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLCMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLCMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaLCMS`

