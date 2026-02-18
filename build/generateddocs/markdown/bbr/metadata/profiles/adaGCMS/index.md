
# ADA GC-MS Profile (Schema)

`cdif.bbr.metadata.profiles.adaGCMS` *v0.1*

Technique-specific profile for Gas Chromatography Mass Spectrometry (GC-MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA GC-MS Profile

Technique-specific metadata profile for Gas Chromatography Mass Spectrometry (GC-MS) products in the Astromat Data Archive. Gas chromatography mass spectrometry analysis.

## Product Types
- `ada:GCMSCollection`
- `ada:GCMSCube`
- `ada:GCGCMSCollection`

## Valid Component Types
- `ada:GCMSCollection`
- `ada:GCMSCube`
- `ada:GCGCMSCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### GC-MS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:GCMSCollection", "ada:DataDeliveryPackage"],
  "schema:name": "GC-MS Analysis of Sample",
  "schema:description": "Gas Chromatography Mass Spectrometry (GC-MS) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaGCMS/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:GCMSCollection",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "GC-MS Analysis of Sample",
  "schema:description": "Gas Chromatography Mass Spectrometry (GC-MS) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:GCMSCollection" ;
    ns1:description "Gas Chromatography Mass Spectrometry (GC-MS) data" ;
    ns1:name "GC-MS Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA GC-MS Product Profile
description: Technique-specific profile for Gas Chromatography Mass Spectrometry (GC-MS)
  products. Extends the base ADA product profile with constraints on valid GC-MS component
  types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a GC-MS product type identifier.
      contains:
        enum:
        - ada:GCMSCollection
        - ada:GCMSCube
        - ada:GCGCMSCollection
        - Gas Chromatography-Mass Spectrometry
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
                      - ada:GCMSCollection
                      - ada:GCMSCube
                      - ada:GCGCMSCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaGCMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaGCMS/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaGCMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaGCMS`

