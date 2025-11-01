
# schema additionalProperty properties (Schema)

`ogc.bbr.test.properties.additionalProperty` *v0.1*

Schema for a schema:PropertyValue used to specify a property of an element that is not defined in the JSON schema..

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person properties

Defines a set of properties for use describing a person for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example additional property.
Example of soft-typed additional property implementation, based on schema.org PropertyValue
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "nxs": "http://purl.org/nexusformat/definitions/"
    },
    "@id": "ex:exampleAdditionalProperty_lkj09",
    "@type": "schema:PropertyValue",
    "schema:propertyID": [
        "nxs:Field/NXsource/probe",
        {
            "@id": "ex:addPropdefinedTerm_zZc",
            "@type": "schema:DefinedTerm",
            "schema:name":"probe",
            "schema:identifier": {
                "@id": "ex:addPropIDPropertyValue_53yh",
                "@type": "schema:PropertyValue",
                "schema:propertyID":"httpUri",
                "schema:url": "http://ogc.org/defs/rt45347278"
            },
            "schema:inDefinedTermSet": "http://ogc.org/defs"
        }
    ],
    "schema:name": "Probe type",
    "schema:value": "x-ray"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/additionalProperty/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "nxs": "http://purl.org/nexusformat/definitions/"
    }
  ],
  "@id": "ex:exampleAdditionalProperty_lkj09",
  "@type": "schema:PropertyValue",
  "schema:propertyID": [
    "nxs:Field/NXsource/probe",
    {
      "@id": "ex:addPropdefinedTerm_zZc",
      "@type": "schema:DefinedTerm",
      "schema:name": "probe",
      "schema:identifier": {
        "@id": "ex:addPropIDPropertyValue_53yh",
        "@type": "schema:PropertyValue",
        "schema:propertyID": "httpUri",
        "schema:url": "http://ogc.org/defs/rt45347278"
      },
      "schema:inDefinedTermSet": "http://ogc.org/defs"
    }
  ],
  "schema:name": "Probe type",
  "schema:value": "x-ray"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:exampleAdditionalProperty_lkj09 a schema1:PropertyValue ;
    schema1:name "Probe type" ;
    schema1:propertyID ex:addPropdefinedTerm_zZc,
        "nxs:Field/NXsource/probe" ;
    schema1:value "x-ray" .

ex:addPropIDPropertyValue_53yh a schema1:PropertyValue ;
    schema1:propertyID "httpUri" ;
    schema1:url "http://ogc.org/defs/rt45347278" .

ex:addPropdefinedTerm_zZc a schema1:DefinedTerm ;
    schema1:identifier ex:addPropIDPropertyValue_53yh ;
    schema1:inDefinedTermSet "http://ogc.org/defs" ;
    schema1:name "probe" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: additionalProperty PropertyValue
description: 'PropertyValue values required to define a soft-typed property with a
  value. '
properties:
  '@type':
    type: string
    const: schema:PropertyValue
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
  schema:name:
    type: string
  schema:value:
    type: string
required:
- schema:name
- schema:value
$defs:
  DefinedTerm:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: http://purl.org/nexusformat/definitions/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/additionalProperty/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/additionalProperty/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/additionalProperty/context.jsonld)

## Sources

* [schema.org](https://schema.org/additionalProperty)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/additionalProperty`

