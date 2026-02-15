
# ADA AIVA Profile (Schema)

`cdif.bbr.metadata.profiles.adaAIVA` *v0.1*

Technique-specific profile for AI-driven Visual Analysis (AIVA) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA AIVA Profile

Technique-specific metadata profile for AI-driven Visual Analysis (AIVA) products in the Astromat Data Archive. AI-driven visual analysis imaging.

## Product Types
- `ada:AIVAImage`
- `ada:AIVAImageCollection`

## Valid Component Types
- `ada:AIVAImage`
- `ada:AIVAImageCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### AIVA Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:AIVAImage", "ada:DataDeliveryPackage"],
  "schema:name": "AIVA Analysis of Sample",
  "schema:description": "AI-driven Visual Analysis (AIVA) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA AIVA Product Profile
description: Technique-specific profile for AI-driven Visual Analysis (AIVA) products.
  Extends the base ADA product profile with constraints on valid AIVA component types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a AIVA product type identifier.
      contains:
        enum:
        - ada:AIVAImage
        - ada:AIVAImageCollection
        - Advanced Imaging & Visualization of Astromaterials
        - Advanced Imaging &amp; Visualization of Astromaterials
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:AIVAImage
                    - ada:AIVAImageCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaAIVA/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaAIVA/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaAIVA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaAIVA`

