
# Identifier (Schema)

`ogc.bbr.test.properties.identifier` *v0.1*

schema.org properties for an identifier implemented as schema.org/PropertyValue.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Identifier Properties

Defines a set of properties to document an identifier, based on schema.org model, for use with schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example identifier .
Example identifier instance.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": "schema:PropertyValue",
    "schema:propertyID": "example identifier",
    "schema:value": "wwyPcWQqoT",
    "schema:url": "https://identifier.org/uri:test:wwyPcWQqoT"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": "schema:PropertyValue",
  "schema:propertyID": "example identifier",
  "schema:value": "wwyPcWQqoT",
  "schema:url": "https://identifier.org/uri:test:wwyPcWQqoT"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:PropertyValue ;
    schema1:propertyID "example identifier" ;
    schema1:url "https://identifier.org/uri:test:wwyPcWQqoT" ;
    schema1:value "wwyPcWQqoT" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Properties for a schema.org identifier
type: object
properties:
  '@type':
    type: string
    const: schema:PropertyValue
  schema:propertyID:
    type: string
    description: identifier for the identifier schema, e.g. DOI, ARK.  Get values
      from https://registry.identifiers.org/registry/ for interoperability
  schema:value:
    type: string
    description: the identifier string. E.g. 10.5066/F7VX0DMQ
  schema:url:
    type: string
    format: uri
    description: 'web-resolveable string for the identifier; host name part is location
      of a resolver that will return some representation for the given identifier
      value. E.g. https://doi.org/10.5066/F7VX0DMQ '
allOf:
- required:
  - '@type'
- anyOf:
  - required:
    - schema:value
  - required:
    - schema:url
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/context.jsonld)

## Sources

* [schema.org](https://schema.org/PropertyValue)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/identifier`

