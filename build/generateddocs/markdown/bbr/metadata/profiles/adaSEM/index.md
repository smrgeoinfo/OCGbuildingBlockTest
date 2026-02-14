
# ADA SEM Profile (Schema)

`cdif.bbr.metadata.profiles.adaSEM` *v0.1*

Technique-specific profile for Scanning Electron Microscopy (SEM) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA SEM Profile

Technique-specific metadata profile for Scanning Electron Microscopy (SEM) products in the Astromat Data Archive. Scanning electron microscopy imaging and analysis.

## Product Types
- `ada:SEMImageCollection`
- `ada:SEMImageMap`
- `ada:SEMEBSDGrainImage`
- `ada:SEMEBSDGrainImageMap`
- `ada:SEMEBSDGrainImageMapCube`
- `ada:SEMEDSElementalMap`
- `ada:SEMEDSElementalMaps`
- `ada:SEMEDSElementalMapsCube`
- `ada:SEMEDSPointData`
- `ada:SEMEDSPointDataCollection`
- `ada:SEMEDSPointDataCube`
- `ada:SEMHRCLImage`
- `ada:SEMHRCLMap`
- `ada:SEMHRCLCube`

## Valid Component Types
- `ada:SEMImageCollection`
- `ada:SEMImageMap`
- `ada:SEMEBSDGrainImage`
- `ada:SEMEBSDGrainImageMap`
- `ada:SEMEBSDGrainImageMapCube`
- `ada:SEMEDSElementalMap`
- `ada:SEMEDSElementalMaps`
- `ada:SEMEDSElementalMapsCube`
- `ada:SEMEDSPointData`
- `ada:SEMEDSPointDataCollection`
- `ada:SEMEDSPointDataCube`
- `ada:SEMHRCLImage`
- `ada:SEMHRCLMap`
- `ada:SEMHRCLCube`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### SEM Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:SEMImageCollection", "ada:DataDeliveryPackage"],
  "schema:name": "SEM Analysis of Sample",
  "schema:description": "Scanning Electron Microscopy (SEM) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA SEM Product Profile
description: Technique-specific profile for Scanning Electron Microscopy (SEM) products.
  Extends the base ADA product profile with constraints on valid SEM component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a SEM product type identifier.
      contains:
        enum:
        - ada:SEMImageCollection
        - ada:SEMImageMap
        - ada:SEMEBSDGrainImage
        - ada:SEMEBSDGrainImageMap
        - ada:SEMEBSDGrainImageMapCube
        - ada:SEMEDSElementalMap
        - ada:SEMEDSElementalMaps
        - ada:SEMEDSElementalMapsCube
        - ada:SEMEDSPointData
        - ada:SEMEDSPointDataCollection
        - ada:SEMEDSPointDataCube
        - ada:SEMHRCLImage
        - ada:SEMHRCLMap
        - ada:SEMHRCLCube
        - Scanning electron microscopy
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:SEMImageCollection
                    - ada:SEMImageMap
                    - ada:SEMEBSDGrainImage
                    - ada:SEMEBSDGrainImageMap
                    - ada:SEMEBSDGrainImageMapCube
                    - ada:SEMEDSElementalMap
                    - ada:SEMEDSElementalMaps
                    - ada:SEMEDSElementalMapsCube
                    - ada:SEMEDSPointData
                    - ada:SEMEDSPointDataCollection
                    - ada:SEMEDSPointDataCube
                    - ada:SEMHRCLImage
                    - ada:SEMHRCLMap
                    - ada:SEMHRCLCube
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaSEM/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaSEM/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/_sources/profiles/adaSEM/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaSEM`

