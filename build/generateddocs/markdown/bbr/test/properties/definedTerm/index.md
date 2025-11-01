
# Defined Term (Schema)

`ogc.bbr.test.properties.definedTerm` *v0.1*

Schema defining propertis of a term from a named or identified vocabulary, with a label, and URI.Based on Schema.org/definedTerm

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DefinedTerm properties

Defines a set of properties for use describing a schema.org DefinedTerm for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Defined Term examples.
Example Defined Term instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:definedTerm_zZc",
  "@type": "schema:DefinedTerm",
  "schema:name": "TestTerm",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://identifiers.org/scheme/rt45347278",
    "schema:url": "http://ogc.org/defs/rt45347278"
  },
  "schema:inDefinedTermSet": "http://ogc.org/defs",
  "schema:termCode": "TT"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:definedTerm_zZc",
  "@type": "schema:DefinedTerm",
  "schema:name": "TestTerm",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://identifiers.org/scheme/rt45347278",
    "schema:url": "http://ogc.org/defs/rt45347278"
  },
  "schema:inDefinedTermSet": "http://ogc.org/defs",
  "schema:termCode": "TT"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:definedTerm_zZc a schema1:DefinedTerm ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://identifiers.org/scheme/rt45347278" ;
            schema1:url "http://ogc.org/defs/rt45347278" ] ;
    schema1:inDefinedTermSet "http://ogc.org/defs" ;
    schema1:name "TestTerm" ;
    schema1:termCode "TT" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema.org Defined Term schema
type: object
properties:
  '@type':
    const: schema:DefinedTerm
  schema:name:
    type: string
    description: text label for the term that is useful to human user
  schema:identifier:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml
  schema:inDefinedTermSet:
    type: string
    description: Identifier for the controlled vocabulary responsible for this keyword.
  schema:termCode:
    type: string
    description: A representative code for this keyword in the controlled vocabulary
      (Optional).  Analogous to skos:Notation
allOf:
- required:
  - '@type'
- anyOf:
  - required:
    - schema:name
  - required:
    - schema:identifier
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/context.jsonld)

## Sources

* [schema.org](https://schema.org/DefinedTerm)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/definedTerm`

