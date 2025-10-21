
# Agent (Schema)

`ogc.bbr.test.entities.agent` *v0.1*

JSON schema for an agent, imports properties for person, organization, and responsibleParty.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## My Schema

Defines a set of properties that may be used in **any** JSON schema.

> Note these properties may be used in the "properties" sub-component of a GeoJSON object, as a simple object

The numeric properties "b" and "c" have an example SHACL rule that if c is present, then c > b
## Examples

### This is an example with just a description and no code snippets.
This an example.

In **Markdown** format.
#### json
```json
{
  "a": "mynamespace:aThing",
  "b": 23,
  "c": 1
}


```

#### jsonld
```jsonld
{
  "@context": [
    {
      "mynamespace": "http://example.com/mythings/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/entities/agent/context.jsonld"
  ],
  "a": "mynamespace:aThing",
  "b": 23,
  "c": 1
}
```

#### ttl
```ttl


```


### Examples can have content and/or code snippets.
The content of this example. 
#### shell
```shell
echo 'Hello, world!'
```

#### python
```python
print('Hello, world!')
```

#### javascript
```javascript
console.log('Hello, world!')
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

