
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
description: Defines implementation-specific properties for the representation of
  a variable in a dataset. Aligned with CDIF 2026 schema using DDI-CDI flat per-column
  mapping structure.
type: object
properties:
  cdi:index:
    type: integer
    minimum: 0
    description: Non-negative integer that orders the fields in the data structure
      (column number).
  cdi:format:
    type: string
    description: A format for number expressed as a string, or date format like YYYY/MM
      or MM-DD-YY.
  cdi:physicalDataType:
    type: string
  cdi:length:
    type: integer
    description: The column width if the tabular text is fixed width.
  cdi:nullSequence:
    type: string
    description: The value of this property becomes the null annotation for the described
      column.
  cdi:defaultValue:
    type: string
    description: A default string indicating the value to substitute for an empty
      string.
  cdi:scale:
    type: integer
  cdi:decimalPositions:
    type: integer
  cdi:minimumLength:
    type: integer
  cdi:maximumLength:
    type: integer
  cdi:isRequired:
    type: boolean
    default: false
  cdi:formats_InstanceVariable:
    type: object
    description: Reference to a variable defined in schema:variableMeasured.
    properties:
      '@id':
        type: string
        description: This should be a reference to a variable defined in the schema:variableMeasured
          section.
  cdi:defaultDecimalSeparator:
    type: string
  cdi:defaultDigitalGroupSeparator:
    type: string
  cdi:displayLabel:
    type: string
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

