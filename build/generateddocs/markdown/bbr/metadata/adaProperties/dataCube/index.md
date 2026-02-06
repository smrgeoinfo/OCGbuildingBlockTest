
# Data Cube Type (Schema)

`cdif.bbr.metadata.adaProperties.dataCube` *v0.1*

CDI DimensionalDataStructure for multidimensional data

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data Cube Type

Describes multidimensional data structures in ADA metadata. Typed as `ada:dataCube` and `cdi:DimensionalDataStructure`. Supports DimensionComponent, MeasureComponent, and AttributeComponent with value domain specifications and value mappings.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Data Cube Type
description: Multi-dimensional data cube structure using DDI-CDI. Typed as ada:dataCube
  and cdi:StructuredDataSet per CDIF 2026 alignment.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:dataCube
    - contains:
        const: cdi:StructuredDataSet
  componentType:
    anyOf:
    - type: object
      properties:
        '@type':
          enum:
          - ada:GCMSCollection
          - ada:GCMSCube
          - ada:FTICRMSCube
          - ada:LCMSCollection
          - ada:SEMEBSDGrainImageMapCube
          - ada:SEMEDSElementalMapsCube
          - ada:SEMEDSPointDataCube
          - ada:SEMHRCLCube
          - ada:STEMEDSCube
          - ada:STEMEDSTomo
          - ada:STEMEELSCube
          - ada:VNMIRSpectralMap
      required:
      - '@type'
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/l2ms_detail
  dataComponentResource:
    type: string
  cdi:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      allOf:
      - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/physicalMapping/schema.yaml
      - type: object
        properties:
          cdi:locator:
            type: string
            description: String that can be used by software to locate values of the
              variable in this physical dataset.
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/dataCube/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/dataCube/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/dataCube/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/dataCube`

