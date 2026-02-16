
# ADA ARGT Profile (Schema)

`cdif.bbr.metadata.profiles.adaARGT` *v0.1*

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
- `ada:calibrationFile`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`

## Detail Type
`detailARGT`

## Examples

### ARGT Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:ARGTDocument", "ada:DataDeliveryPackage"],
  "schema:name": "ARGT Analysis of Sample",
  "schema:description": "Argon Geochronology and Thermochronology (ARGT) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaARGT/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:ARGTDocument",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "ARGT Analysis of Sample",
  "schema:description": "Argon Geochronology and Thermochronology (ARGT) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:ARGTDocument",
        "ada:DataDeliveryPackage" ;
    ns1:description "Argon Geochronology and Thermochronology (ARGT) data" ;
    ns1:name "ARGT Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ARGT Product Profile
description: Technique-specific profile for Argon Geochronology and Thermochronology
  (ARGT) products. Extends the base ADA product profile with constraints on valid
  ARGT component types and detailARGT requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ARGT product type identifier.
      contains:
        enum:
        - ada:ARGTDocument
        - ada:ARGTCollection
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
                      - ada:calibrationFile
                      - ada:analysisLocation
                      - ada:methodDescription
                      - ada:instrumentMetadata
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaARGT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaARGT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaARGT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaARGT`

