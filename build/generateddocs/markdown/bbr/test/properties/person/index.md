
# Person (Schema)

`ogc.bbr.test.properties.person` *v0.1*

Schema defining propertis of a person, a profile of schema.org/Person.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person properties

Defines a set of properties for use describing a person for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example person.
Example person instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:PersonExample_zZc",
  "@type": "schema:Person",
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": {
    "@type": "schema:Organization",
    "schema:name": "Test organization"
  },
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://doi.org",
    "schema:value": "iY",
    "schema:url": "https://doi.org/iY"
  },
  "schema:contactPoint": {
    "@type": "schema:ContactPoint",
    "schema:email": "joe@bmanuco.org"
  },
  "schema:sameAs": [
    "https://ark.org/46737",
    "uri:test:43737"
  ]
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:PersonExample_zZc",
  "@type": "schema:Person",
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": {
    "@type": "schema:Organization",
    "schema:name": "Test organization"
  },
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://doi.org",
    "schema:value": "iY",
    "schema:url": "https://doi.org/iY"
  },
  "schema:contactPoint": {
    "@type": "schema:ContactPoint",
    "schema:email": "joe@bmanuco.org"
  },
  "schema:sameAs": [
    "https://ark.org/46737",
    "uri:test:43737"
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:PersonExample_zZc a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "Test organization" ] ;
    schema1:alternateName "Test, Joe" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@bmanuco.org" ] ;
    schema1:description "Metadata specialist, based in Portland, Maine" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/iY" ;
            schema1:value "iY" ] ;
    schema1:name "Joe Test" ;
    schema1:sameAs "https://ark.org/46737",
        "uri:test:43737" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: My example schema
type: object
properties:
  '@id':
    type: string
  '@type':
    type: string
    const: schema:Person
  schema:name:
    type: string
    description: string label for person that is meaningful for human users
  schema:description:
    type: string
  schema:identifier:
    description: identifier for person
    anyOf:
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml
    - type: string
  schema:alternateName:
    type: string
    description: other labels by which the person might be known
  schema:affiliation:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/schema.yaml
    description: if affiliation is present, value must be a schema:Organization.
  schema:contactPoint:
    type: object
    properties:
      '@type':
        const: schema:ContactPoint
      schema:email:
        type: string
    description: restrict to email only. Schema.org allows telephone and postal contacts
      as well
  schema:sameAs:
    type: array
    description: other identifiers for the person
    items:
      type: string
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/context.jsonld)

## Sources

* [schema.org](https://schema.org/Person)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/person`

