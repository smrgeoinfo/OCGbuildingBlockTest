
# ADA XRD Profile (Schema)

`cdif.bbr.metadata.profiles.adaXRD` *v0.1*

Technique-specific profile for X-ray Diffraction (XRD) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA XRD Profile

Technique-specific metadata profile for X-ray Diffraction (XRD) products in the Astromat Data Archive. XRD measures the diffraction pattern produced by X-rays interacting with crystalline materials to determine crystal structure, phase identification, and lattice parameters.

## Product Types
- **XRD Tabular** - Diffraction pattern data in tabular format (2-theta vs. intensity)

## Valid Component Types
- `ada:XRDTabular` - Tabular diffraction data with geometry and wavelength detail (xrd_detail)
- `ada:XRDDiffractionPattern` - Diffraction pattern images
- `ada:XRDIndexedImage` - Indexed diffraction pattern images
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:methodDescription` - Method description documents

## Detail Type
`xrd_detail` with properties: `geometry`, `sampleMount`, `stepSize`, `timePerStep`, `wavelength`

## Examples

### XRD Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:XRDTabular", "ada:DataDeliveryPackage"],
  "schema:name": "XRD Analysis of Mineral Sample",
  "schema:description": "X-ray diffraction pattern data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaXRD/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:XRDTabular",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "XRD Analysis of Mineral Sample",
  "schema:description": "X-ray diffraction pattern data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "ada:DataDeliveryPackage",
        "ada:XRDTabular" ;
    schema1:description "X-ray diffraction pattern data" ;
    schema1:name "XRD Analysis of Mineral Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA XRD Product Profile
description: Technique-specific profile for X-ray Diffraction (XRD) products. Extends
  the base ADA product profile with constraints on valid XRD component types and xrd_detail
  requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include an XRD product type identifier.
      contains:
        const: ada:XRDTabular
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:XRDTabular
                    - ada:XRDDiffractionPattern
                    - ada:XRDIndexedImage
                    - ada:instrumentMetadata
                    - ada:methodDescription
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaXRD/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaXRD/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaXRD/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaXRD`

