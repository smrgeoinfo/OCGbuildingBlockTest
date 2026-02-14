
# ADA LIT Profile (Schema)

`cdif.bbr.metadata.profiles.adaLIT` *v0.1*

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
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### LIT Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:LITImage", "ada:DataDeliveryPackage"],
  "schema:name": "LIT Analysis of Sample",
  "schema:description": "Lock-In Thermography (LIT) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA LIT Product Profile
description: Technique-specific profile for Lock-In Thermography (LIT) products. Extends
  the base ADA product profile with constraints on valid LIT component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a LIT product type identifier.
      contains:
        enum:
        - ada:LITImage
        - ada:LIT2DDataCollection
        - ada:LITPolarDataCollection
        - Lock-In Thermography
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:LITImage
                    - ada:LIT2DDataCollection
                    - ada:LITPolarDataCollection
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLIT/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaLIT/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/_sources/profiles/adaLIT/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaLIT`

