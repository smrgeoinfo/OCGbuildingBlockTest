
# Agent (Schema)

`ogc.bbr.test.entities.agent` *v0.1*

JSON schema for an agent, imports properties for person, organization, and responsibleParty.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person, Organization, Responsibility

Defines a set of properties to describe a person, an organization, or one of those in an assigned role (labeled 'responsibility'). 

Imports properties for person, organization and responsibility.  Person and organization can be considered profiles of prov:Agent. Implementation is targeted here for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Simple agent that is a Person..
Example Agent.

In **Markdown** format.
#### json
```json
{
  "@context": {
    "schema": "https://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:AgentExample_zZc",
  "@type": "schema:Person",
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": "some organization",
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": "PropertyValue",
    "propertyID": "https://doi.org",
    "value": "iY",
    "url": "https://doi.org/iY"
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
      "schema": "https://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/entities/agent/context.jsonld",
    {
      "schema": "https://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:AgentExample_zZc",
  "@type": "schema:Person",
  "schema:name": "Joe Test",
  "schema:alternateName": "Test, Joe",
  "schema:affiliation": "some organization",
  "schema:description": "Metadata specialist, based in Portland, Maine",
  "schema:identifier": {
    "@type": "PropertyValue",
    "propertyID": "https://doi.org",
    "value": "iY",
    "url": "https://doi.org/iY"
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
@prefix schema: <https://schema.org/> .

ex:AgentExample_zZc a schema:Person ;
    schema:affiliation "some organization" ;
    schema:alternateName "Test, Joe" ;
    schema:description "Metadata specialist, based in Portland, Maine" ;
    schema:identifier [ a <file:///github/workspace/PropertyValue> ] ;
    schema:name "Joe Test" ;
    schema:sameAs "https://ark.org/46737",
        "uri:test:43737" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Agent entity; can be person, organization or (person or Organization)
  with Role. The third option is represented using schema.org contributor
$definitions:
  Person:
    type: object
    properties:
      $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/schema.yaml
allOf:
- $ref: '#/$definitions/Person'
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/entities/agent/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/entities/agent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "https://schema.org",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/entities/agent/context.jsonld)

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/entities/agent`

