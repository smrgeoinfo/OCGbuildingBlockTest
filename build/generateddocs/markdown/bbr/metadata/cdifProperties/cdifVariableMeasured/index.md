
# VariableMeasured with DDI-CDI extensions (Schema)

`cdif.bbr.metadata.cdifProperties.cdifVariableMeasured` *v0.1*

Schema defining properties for schema.org variableMeasured with some DDI-CDI properties, for implementation of CDIF discovery XAS profile. Implemented as schema.org/PropertyValue

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## additional Property, Property Value properties

Defines a set of properties for use describing a soft-typed PropertyValue for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Use for values of schema:additionalProperty, typically in the context of extension profiles. Not used in CDIF Mandatory or CDIF Optional.
## Examples

### Variable Measured for CDIF XAS.
Implementation of Schema.org PropertyValue as value for variableMeasured property, adding cdi InstanceVariable type and several other properties from DDI-CDI.  For testing with X-Ray Absorbtion profile.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "xas": "https://xas.org/dictionary/"
    },
    "@id": "xas:monochromatorEnergy",
    "@type": [
        "cdi:InstanceVariable",
        "schema:PropertyValue"
    ],
    "schema:name": "energy",
    "schema:alternateName": ["Monochromator energy"],
    "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
    "schema:propertyID": ["xas:monochromatorEnergyConcept"],
    "schema:unitText": "eV",
    "cdi:identifier": "should be URI from nexusFormat organization",
    "cdi:physicalDataType": ["https://www.w3.org/TR/xmlschema-2/#decimal"],
    "cdi:simpleUnitOfMeasure": "eV",
    "cdi:uses": "xas:monochromatorEnergyConcept",
    "cdi:name": "energy",
    "cdi:displayLabel": "monochromator energy"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "xas": "https://xas.org/dictionary/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifVariableMeasured/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://xas.org/dictionary/"
    }
  ],
  "@id": "xas:monochromatorEnergy",
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "schema:name": "energy",
  "schema:alternateName": [
    "Monochromator energy"
  ],
  "schema:description": "missing, definition of what this variable is about (maybe even an iAdopt description",
  "schema:propertyID": [
    "xas:monochromatorEnergyConcept"
  ],
  "schema:unitText": "eV",
  "cdi:identifier": "should be URI from nexusFormat organization",
  "cdi:physicalDataType": [
    "https://www.w3.org/TR/xmlschema-2/#decimal"
  ],
  "cdi:simpleUnitOfMeasure": "eV",
  "cdi:uses": "xas:monochromatorEnergyConcept",
  "cdi:name": "energy",
  "cdi:displayLabel": "monochromator energy"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .

xas:monochromatorEnergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "monochromator energy" ;
    cdi:identifier "should be URI from nexusFormat organization" ;
    cdi:name "energy" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "eV" ;
    cdi:uses "xas:monochromatorEnergyConcept" ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "missing, definition of what this variable is about (maybe even an iAdopt description" ;
    schema1:name "energy" ;
    schema1:propertyID "xas:monochromatorEnergyConcept" ;
    schema1:unitText "eV" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Extends cdif variableMeasured with properties for DDI-CDI InstanceVariable
type: object
properties:
  '@type':
    type: array
    description: require additional type besided schema:PropertyValue required by
      CDIF variableMeasured, so min items should add up to 2 (we'll see if this works....)
    items:
      type: string
      enum:
      - schema:PropertyValue
      - cdi:InstanceVariable
    minItems: 2
  cdi:identifier:
    type: string
  cdi:physicalDataType:
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a skos concept for the data type
      - $ref: '#/$defs/DefinedTerm'
    description: identifier or name for the data type concept.
  cdi:intendedDataType:
    type: string
    description: The intended data type for values of this variable, from DDI-CDI
      RepresentedVariable.hasIntendedDataType. Recommended values are XML Schema datatypes
      (e.g. https://www.w3.org/TR/xmlschema-2/#decimal).
  cdi:role:
    type: string
    enum:
    - MeasureComponent
    - AttributeComponent
    - DimensionComponent
    - DescriptorComponent
    - ReferenceValueComponent
    description: Specifies the relation of the variable to the data structure, corresponding
      to DDI-CDI DataStructureComponent subtypes.
  cdi:describedUnitOfMeasure:
    description: A structured unit of measure from a controlled vocabulary, from DDI-CDI
      RepresentedVariable.describedUnitOfMeasure.
    $ref: '#/$defs/DefinedTerm'
  cdi:simpleUnitOfMeasure:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the data type
    - $ref: '#/$defs/DefinedTerm'
  cdi:uses:
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a skos concept for the property
      - $ref: '#/$defs/DefinedTerm'
    description: Essentially the same as schema:propertyID. References to concepts
      that this variable measures or represents.
  cdi:name:
    type: string
    description: DDI-CDI Concept.name. The name of this variable in the DDI-CDI model.
  cdi:displayLabel:
    type: string
    description: DDI-CDI Concept.displayLabel. A human-readable label for display
      purposes.
$defs:
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
allOf:
- required:
  - '@type'
  - cdi:physicalDataType
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  spdx: http://spdx.org/rdf/terms#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  skos: http://www.w3.org/2004/02/skos/core#
  xas: https://xas.org/dictionary/
  nxs: http://purl.org/nexusformat/definitions/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifVariableMeasured/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifVariableMeasured/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifVariableMeasured/context.jsonld)

## Sources

* [schema.org](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifVariableMeasured`

