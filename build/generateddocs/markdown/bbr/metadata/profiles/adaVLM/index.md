
# ADA VLM Profile (Schema)

`cdif.bbr.metadata.profiles.adaVLM` *v0.1*

Technique-specific profile for Visible Light Microscopy (VLM) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA VLM Profile

Technique-specific metadata profile for Visible Light Microscopy (VLM) products in the Astromat Data Archive. Visible light microscopy imaging.

## Product Types
- `ada:VLMImage`
- `ada:VLMImageCollection`

## Valid Component Types
- `ada:VLMImage`
- `ada:VLMImageCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### VLM Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:VLMImage", "ada:DataDeliveryPackage"],
  "schema:name": "VLM Analysis of Sample",
  "schema:description": "Visible Light Microscopy (VLM) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA VLM Product Profile
description: Technique-specific profile for Visible Light Microscopy (VLM) products.
  Extends the base ADA product profile with constraints on valid VLM component types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a VLM product type identifier.
      contains:
        enum:
        - ada:VLMImage
        - ada:VLMImageCollection
        - Visible Light Microscopy
        - Visible Light Microscopy Basemap
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:VLMImage
                    - ada:VLMImageCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVLM/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVLM/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaVLM/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaVLM`

