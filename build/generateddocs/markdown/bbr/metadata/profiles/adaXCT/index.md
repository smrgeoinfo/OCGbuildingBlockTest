
# ADA XCT Profile (Schema)

`cdif.bbr.metadata.profiles.adaXCT` *v0.1*

Technique-specific profile for X-ray Computed Tomography (XCT) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA XCT Profile

Technique-specific metadata profile for X-ray Computed Tomography (XCT) products in the Astromat Data Archive. X-ray computed tomography 3D imaging.

## Product Types
- `ada:XCTImageCollection`

## Valid Component Types
- `ada:XCTImageCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailXCT`

## Examples

### XCT Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:XCTImageCollection", "ada:DataDeliveryPackage"],
  "schema:name": "XCT Analysis of Sample",
  "schema:description": "X-ray Computed Tomography (XCT) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaXCT/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:XCTImageCollection",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "XCT Analysis of Sample",
  "schema:description": "X-ray Computed Tomography (XCT) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:XCTImageCollection" ;
    ns1:description "X-ray Computed Tomography (XCT) data" ;
    ns1:name "XCT Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA XCT Product Profile
description: Technique-specific profile for X-ray Computed Tomography (XCT) products.
  Extends the base ADA product profile with constraints on valid XCT component types
  and detailXCT requirements.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a XCT product type identifier.
      contains:
        enum:
        - ada:XCTImageCollection
        - X-ray computed tomography
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
                      - ada:XCTImageCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaXCT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaXCT/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaXCT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaXCT`

