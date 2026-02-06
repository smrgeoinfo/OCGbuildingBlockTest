
# VariableMeasured (Schema)

`cdif.bbr.metadata.schemaorgProperties.variableMeasured` *v0.1*

Schema defining propertis for schema.org varialbleMeasured as defined for CDIF discovery. Implemented as schema.org/PropertyValue

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## additional Property, Property Value properties

Defines a set of properties for use describing a soft-typed PropertyValue for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Use for values of schema:additionalProperty, typically in the context of extension profiles. Not used in CDIF Mandatory or CDIF Optional.
## Examples

### Variable Measured.
Implementation of Schema.org PropertyValue as value for variableMeasured property.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": ["schema:PropertyValue"],
    "@id": "ex:variableMeasured_346",
    "schema:name": "example variable measured",
    "schema:description": "description missing",
    "schema:propertyID": [
        {
            "@id": "ex:definedTerm_zZc",
            "@type": "schema:DefinedTerm",
            "schema:name": "Temperature",
            "schema:identifier": {
                "@id": "ex:tempTerm_246u",
                "@type": "schema:PropertyValue",
                "schema:propertyID": "http URI",
                "schema:url": "http://ogc.org/defs/PHlSkPJvxy"
            },
            "schema:inDefinedTermSet": "http://ogc.org/defs",
            "schema:termCode": "T"
        }
    ],
    "schema:measurementTechnique": "thermometer",
    "schema:unitText": "deg C",
    "schema:unitCode": "C",
    "schema:minValue": 0,
    "schema:maxValue": 200
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": [
    "schema:PropertyValue"
  ],
  "@id": "ex:variableMeasured_346",
  "schema:name": "example variable measured",
  "schema:description": "description missing",
  "schema:propertyID": [
    {
      "@id": "ex:definedTerm_zZc",
      "@type": "schema:DefinedTerm",
      "schema:name": "Temperature",
      "schema:identifier": {
        "@id": "ex:tempTerm_246u",
        "@type": "schema:PropertyValue",
        "schema:propertyID": "http URI",
        "schema:url": "http://ogc.org/defs/PHlSkPJvxy"
      },
      "schema:inDefinedTermSet": "http://ogc.org/defs",
      "schema:termCode": "T"
    }
  ],
  "schema:measurementTechnique": "thermometer",
  "schema:unitText": "deg C",
  "schema:unitCode": "C",
  "schema:minValue": 0,
  "schema:maxValue": 200
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:variableMeasured_346 a schema1:PropertyValue ;
    schema1:description "description missing" ;
    schema1:maxValue 200 ;
    schema1:measurementTechnique "thermometer" ;
    schema1:minValue 0 ;
    schema1:name "example variable measured" ;
    schema1:propertyID ex:definedTerm_zZc ;
    schema1:unitCode "C" ;
    schema1:unitText "deg C" .

ex:definedTerm_zZc a schema1:DefinedTerm ;
    schema1:identifier ex:tempTerm_246u ;
    schema1:inDefinedTermSet "http://ogc.org/defs" ;
    schema1:name "Temperature" ;
    schema1:termCode "T" .

ex:tempTerm_246u a schema1:PropertyValue ;
    schema1:propertyID "http URI" ;
    schema1:url "http://ogc.org/defs/PHlSkPJvxy" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: CDIF schema.org implemenation of PropertyValue to use as values for variableMeasured
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:PropertyValue
    minItems: 1
  '@id':
    type: string
  schema:name:
    type: string
    description: this is the string label that is expected to be associated with the
      variable in the dataset serialization
  schema:description:
    type: string
    default: missing
  schema:propertyID:
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
    description: identifier or name for the property concept quantified by the values
      in this variable slot. Multiple values can specify the property at different
      levels of granularity.
  schema:measurementTechnique:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the property
    - $ref: '#/$defs/DefinedTerm'
    description: A text description of the measurement method used to determine values
      for this variable. If standard measurement protocols are defined and registered,
      these can be identified via http URI's.
  schema:unitText:
    type: string
    description: A string that identifies a unit of measurement that applies to all
      values for this variable.
  schema:unitCode:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the property
    - $ref: '#/$defs/DefinedTerm'
    description: Value is expected to be TEXT or URL. We recommend providing an HTTP
      URI that identifies a unit of measure from a vocabulary accessible on the web.
      The QUDT unit vocabulary provides and extensive set of registered units of measure
      that can be used to populate the schema:unitCode property to specify the units
      of measure used to report datavalues when that is appropriate.
  schema:minValue:
    type: number
    description: ' If the value for the variable is numeric, this is the minimum value
      that occurs in the dataset. Not useful for other value types.'
  schema:maxValue:
    type: number
    description: ' If the value for the variable is numeric, this is the maximum value
      that occurs in the dataset. Not useful for other value types.'
  schema:url:
    type: string
    description: Any schema:Thing can have a URL property, but because the value is
      simply a url the relationship of the linked resource can not be expressed. Usage
      is optional. The recommendation is that schema:url should link to a web page
      that would be useful for a person to interpret the variable, but is not intended
      to be machine-actionable.
$defs:
  DefinedTerm:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
allOf:
- required:
  - '@type'
  - schema:name
  - schema:description
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/context.jsonld)

## Sources

* [schema.org](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/schemaorgProperties/variableMeasured`

