
# Physical Mapping Type (Schema)

`cdif.bbr.metadata.adaProperties.physicalMapping` *v0.1*

DDI-CDI variable mapping for data structure components

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Physical Mapping Type

Describes DDI-CDI data structure mapping for tabular data files. Uses the WideDataStructure pattern with DataStructureComponents that can be IdentifierComponent, MeasureComponent, or AttributeComponent. Each component includes ValueMapping for physical data layout.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Physical Mapping Type
description: DDI-CDI data structure description for tabular data using WideDataStructure
  with DataStructureComponents including IdentifierComponent, MeasureComponent, and
  AttributeComponent with ValueMapping.
type: object
properties:
  '@type':
    const: cdi:WideDataStructure
  cdi:has_DataStructureComponent:
    type: array
    items:
      type: object
      properties:
        '@id':
          type: string
        '@type':
          oneOf:
          - const: cdi:IdentifierComponent
          - const: cdi:MeasureComponent
          - const: cdi:AttributeComponent
        schema:name:
          type: string
          description: Label for this component in the datafile; overrides name in
            associated InstanceVariable if specified.
        cdi:isDefinedBy_InstanceVariable:
          type: object
          description: Use @id to reference one of the variables defined in the measuredVariable
            section at the product level.
          properties:
            '@id':
              type: string
        cdi:qualifies:
          type: object
          description: Only for Attribute components, use @id to link to the component
            the attribute qualifies.
          properties:
            '@id':
              type: string
        cdi:has:
          type: object
          description: If isDelimited is false, cdi:length is required.
          properties:
            '@type':
              const: cdi:ValueMapping
            cdi:hasIndex:
              description: Column number in the table layout
              type: integer
            cdi:length:
              description: Number of characters in this column
              type: integer
            cdi:physicalDataType:
              type: string
  allowsDuplicates:
    type: boolean
    description: Can rows in the table have identical values
    default: false
  arrayBase:
    type: string
    enum:
    - '0'
    - '1'
    description: If 0, then left most column is column 0
  commentPrefix:
    type: string
    description: Lines beginning with this string will be ignored
  headerRowCount:
    type: integer
    description: Number of rows in the file to skip before data start
  isDelimited:
    type: boolean
  delimiter:
    type: string
    description: Required if isDelimited is true
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/physicalMapping/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/physicalMapping/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/physicalMapping/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/physicalMapping`

