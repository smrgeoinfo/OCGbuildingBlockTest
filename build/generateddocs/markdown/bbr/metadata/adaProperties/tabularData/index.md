
# Tabular Data Type (Schema)

`cdif.bbr.metadata.adaProperties.tabularData` *v0.1*

CDI PhysicalDataSet for tabular/structured data files

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Tabular Data Type

Describes tabular/structured data files in ADA metadata. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Tabular Data Type
description: Tabular/structured data files typed as cdi:PhysicalDataSet and ada:tabularData.
  Includes DDI-CDI WideDataStructure for column layout description.
type: object
properties:
  '@type':
    const:
    - cdi:PhysicalDataSet
    - ada:tabularData
  componentType:
    anyOf:
    - type: object
      properties:
        '@type':
          enum:
          - ada:AMSRawData
          - ada:AMSProcessedData
          - ada:DSCResultsTabular
          - ada:FTICRMSTabular
          - ada:GPYCProcessedTabular
          - ada:GPYCRawTabular
          - ada:HRICPMSProcessed
          - ada:HRICPMSRaw
          - ada:ICPOESIntermediateTabular
          - ada:ICPOESProcessedTabular
          - ada:ICPOESRawTabular
          - ada:ICTabular
          - ada:MCICPMSTabular
          - ada:NGNSMSRaw
          - ada:NGNSMSProcessed
          - ada:QICPMSProcessedTabular
          - ada:QICPMSRawTabular
          - ada:RAMANRawTabular
          - ada:RITOFNGMSTabular
          - ada:RITOFNGMSCollection
          - ada:SEMEDSPointData
          - ada:SIMSTabular
          - ada:STEMEDSTabular
          - ada:STEMEELSTabular
          - ada:SVRUECTabular
          - ada:XANESRawTabular
          - ada:XANESProcessedTabular
      required:
      - '@type'
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/dsc_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/eairms_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/empa_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/laf_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/nanosims_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/nanoir_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/psfd_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/vnmir_detail
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml#/$defs/xrd_detail
  cdi:isStructuredBy:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/physicalMapping/schema.yaml
  countRows:
    type: integer
  countColumns:
    type: integer
  xCoordCol:
    description: Column name for X coordinates
    type: string
  yCoordCol:
    type: string
  zCoordCol:
    type: string
  coordUnits:
    type: string
  spatialRegistration:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/spatialRegistration/schema.yaml
required:
- '@type'
- componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/tabularData/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/tabularData/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/tabularData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/tabularData`

