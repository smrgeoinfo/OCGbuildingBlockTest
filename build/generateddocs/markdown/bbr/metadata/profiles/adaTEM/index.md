
# ADA TEM Profile (Schema)

`cdif.bbr.metadata.profiles.adaTEM` *v0.1*

Technique-specific profile for Transmission Electron Microscopy (TEM) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA TEM Profile

Technique-specific metadata profile for Transmission Electron Microscopy (TEM) products in the Astromat Data Archive. Transmission electron microscopy imaging and spectroscopy.

## Product Types
- `ada:TEMImage`
- `ada:TEMPatternsImage`
- `ada:TEMEDSImageCollection`
- `ada:STEMImage`
- `ada:STEMEDSTabular`
- `ada:STEMEDSCube`
- `ada:STEMEDSTomo`
- `ada:STEMEELSTabular`
- `ada:STEMEELSCube`

## Valid Component Types
- `ada:TEMImage`
- `ada:TEMPatternsImage`
- `ada:TEMEDSImageCollection`
- `ada:STEMImage`
- `ada:STEMEDSTabular`
- `ada:STEMEDSCube`
- `ada:STEMEDSTomo`
- `ada:STEMEELSTabular`
- `ada:STEMEELSCube`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### TEM Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:TEMImage", "ada:DataDeliveryPackage"],
  "schema:name": "TEM Analysis of Sample",
  "schema:description": "Transmission Electron Microscopy (TEM) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA TEM Product Profile
description: Technique-specific profile for Transmission Electron Microscopy (TEM)
  products. Extends the base ADA product profile with constraints on valid TEM component
  types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a TEM product type identifier.
      contains:
        enum:
        - ada:TEMImage
        - ada:TEMPatternsImage
        - ada:TEMEDSImageCollection
        - ada:STEMImage
        - ada:STEMEDSTabular
        - ada:STEMEDSCube
        - ada:STEMEDSTomo
        - ada:STEMEELSTabular
        - ada:STEMEELSCube
        - Transmission Electron Microscopy
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:TEMImage
                    - ada:TEMPatternsImage
                    - ada:TEMEDSImageCollection
                    - ada:STEMImage
                    - ada:STEMEDSTabular
                    - ada:STEMEDSCube
                    - ada:STEMEDSTomo
                    - ada:STEMEELSTabular
                    - ada:STEMEELSCube
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaTEM/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaTEM/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/_sources/profiles/adaTEM/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaTEM`

