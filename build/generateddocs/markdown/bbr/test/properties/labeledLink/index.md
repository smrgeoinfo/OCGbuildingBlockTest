
# Labeled Link (Schema)

`ogc.bbr.test.properties.labeledLink` *v0.1*

Schema defining propertis for a labeled link, implemented using a profile of schema.org/CreativeWork.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Labeled Link properties

Defines a set of properties for use describing a web link (url) with a label to indicate the target, like an html:anchor. For the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Labeled Link building block.
Example labeled link instance.

In **Markdown** format.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:LabeledLinkExample_zZc",
    "@type": "schema:CreativeWork",
    "schema:name": "Some relsted resource",
    "schema:description": "URL to get the related resource",
    "schema:url": "https://example.org/relatedresoruce/2342747"
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "https://schema.org"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:LabeledLinkExample_zZc",
  "@type": "schema:CreativeWork",
  "schema:name": "Some relsted resource",
  "schema:description": "URL to get the related resource",
  "schema:url": "https://example.org/relatedresoruce/2342747"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:LabeledLinkExample_zZc a schema1:CreativeWork ;
    schema1:description "URL to get the related resource" ;
    schema1:name "Some relsted resource" ;
    schema1:url "https://example.org/relatedresoruce/2342747" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema for a labeled link, a profile of schema.org/CreativeWork
type: object
properties:
  '@type':
    type: string
    default: schema:CreativeWork
    const: schema:CreativeWork
  schema:name:
    type: string
  schema:description:
    type: string
  schema:url:
    type: string
    format: uri
required:
- '@type'
- schema:url
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/labeledLink/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/labeledLink/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/labeledLink/context.jsonld)

## Sources

* [schema.org](https://schema.org/CreativeWork)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/labeledLink`

