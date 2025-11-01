
# VariableMeasured for XAS profile (Schema)

`ogc.bbr.test.xasProfile.xasVariableMeasured` *v0.1*

Schema defining propertis for schema.org varialbleMeasured as defined for CDIF discovery XAS profile. Implemented as schema.org/PropertyValue

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## additional Property, Property Value properties

Defines a set of properties for use describing a soft-typed PropertyValue for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Use for values of schema:additionalProperty, typically in the context of extension profiles. Not used in CDIF Mandatory or CDIF Optional.
## Examples

### Variable Measured for CDIF XAS.
Implementation of Schema.org PropertyValue as value for variableMeasured property in X-Ray Absorbtion profile. Profile adds InstanceVariable type and several properties from DDI-CDI.
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
    "schema:alternateName": "Monochromator energy",
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
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/xasProfile/xasVariableMeasured/context.jsonld",
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
  "schema:alternateName": "Monochromator energy",
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
    allOf:
    - contains:
        const: cdi:InstanceVariable
    - contains:
        const: schema:PropertyValue
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
    type: string
    description: reference to a skos concept for the data type
  cdi:name:
    type: string
  cdi:displayLabel:
    type: string
$defs:
  DefinedTerm:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.yaml
allOf:
- required:
  - '@type'
  - cdi:physicalDataType
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/variableMeasured/schema.yaml
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/xasProfile/xasVariableMeasured/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/xasProfile/xasVariableMeasured/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/xasProfile/xasVariableMeasured/context.jsonld)

## Sources

* [schema.org](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/xasProfile/xasVariableMeasured`

