
# Funding (Schema)

`ogc.bbr.test.properties.funder` *v0.1*

properties for acknowledging funding, CDIF profile of schema.org/funding and schema.org/MonetaryGrant.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Funding properties

Defines a set of properties for use funding that supported development or maintenance of a resource, for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Based on schema.org/MonetaryGrant
## Examples

### Example Funder.
Example Funder instance.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": "schema:MonetaryGrant",
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "NSF award number",
        "schema:value": "2227407",
        "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407"
    },
    "schema:name": "Big Bucks for Research",
    "schema:funder": {"@id": "https://ror.org/021nxhr62"}
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/funder/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": "schema:MonetaryGrant",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "NSF award number",
    "schema:value": "2227407",
    "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407"
  },
  "schema:name": "Big Bucks for Research",
  "schema:funder": {
    "@id": "https://ror.org/021nxhr62"
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:MonetaryGrant ;
    schema1:funder <https://ror.org/021nxhr62> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "NSF award number" ;
            schema1:url "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2227407" ;
            schema1:value "2227407" ] ;
    schema1:name "Big Bucks for Research" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Funding acknowledgement properties, profile of schema.org/MonetaryGrant
type: object
properties:
  '@type':
    type: string
    default: schema:MonetaryGrant
    const: schema:MonetaryGrant
  schema:identifier:
    $ref: '#/$defs/Identifier'
    description: identifier for a particular grant
  schema:name:
    type: string
    description: title of the grant
  schema:funder:
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
          description: a identifier for an agent defined in this metadata, or externally;
            must be dereferenceable
    - $ref: '#/$defs/Person'
    - $ref: '#/$defs/Organization'
allOf:
- required:
  - schema:funder
- anyOf:
  - required:
    - schema:identifier
  - required:
    - schema:name
$defs:
  Person:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/schema.yaml
  Organization:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/schema.yaml
  Identifier:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/funder/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/funder/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/funder/context.jsonld)

## Sources

* [schema.org](https://schema.org/funding)
* [schema.org](https://schema.org/MonetaryGrant)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/funder`

