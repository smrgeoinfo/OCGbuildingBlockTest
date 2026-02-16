
# Simple quality measurement properties (Schema)

`cdif.bbr.metadata.qualityProperties.qualityMeasure` *v0.1*

Schema defining properties for documenting a quality measuremenet associated with a resource.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person properties

Defines a set of properties for use describing a person for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example quality measure.
Example quality measure
#### json
```json
{
    "@type": "dqv:QualityMeasurement",
    "dqv:isMeasurementOf": {
        "@type": "schema:DefinedTerm",
        "schema:name": "LBp",
        "schema:identifier": "qMsuTaeO",
        "schema:inDefinedTermSet": "GCjNHSplcIDSd",
        "schema:termCode": "kVavhujDLioBbZc"
    },
    "dqv:value": {
        "@type": "schema:DefinedTerm",
        "schema:name": "aZrfr",
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "bOQUqI",
            "schema:value": "dzkwRNhKqfDVhOu",
            "schema:url": "http://example.com/resource?foo=bar#fragment"
        },
        "schema:inDefinedTermSet": "YYdmhomhxBnNBic",
        "schema:termCode": "OgZwkLzhtqNSCcvMYKT"
    }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/context.jsonld"
  ],
  "@type": "dqv:QualityMeasurement",
  "dqv:isMeasurementOf": {
    "@type": "schema:DefinedTerm",
    "schema:name": "LBp",
    "schema:identifier": "qMsuTaeO",
    "schema:inDefinedTermSet": "GCjNHSplcIDSd",
    "schema:termCode": "kVavhujDLioBbZc"
  },
  "dqv:value": {
    "@type": "schema:DefinedTerm",
    "schema:name": "aZrfr",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "bOQUqI",
      "schema:value": "dzkwRNhKqfDVhOu",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    },
    "schema:inDefinedTermSet": "YYdmhomhxBnNBic",
    "schema:termCode": "OgZwkLzhtqNSCcvMYKT"
  }
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .
@prefix ns2: <dqv:> .

[] a ns2:QualityMeasurement ;
    ns2:isMeasurementOf [ a ns1:DefinedTerm ;
            ns1:identifier "qMsuTaeO" ;
            ns1:inDefinedTermSet "GCjNHSplcIDSd" ;
            ns1:name "LBp" ;
            ns1:termCode "kVavhujDLioBbZc" ] ;
    ns2:value [ a ns1:DefinedTerm ;
            ns1:identifier [ a ns1:PropertyValue ;
                    ns1:propertyID "bOQUqI" ;
                    ns1:url "http://example.com/resource?foo=bar#fragment" ;
                    ns1:value "dzkwRNhKqfDVhOu" ] ;
            ns1:inDefinedTermSet "YYdmhomhxBnNBic" ;
            ns1:name "aZrfr" ;
            ns1:termCode "OgZwkLzhtqNSCcvMYKT" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for simple quality measure property
type: object
properties:
  '@type':
    const: dqv:QualityMeasurement
  dqv:isMeasurementOf:
    description: specify the quality measure that is reported, by name, with an ID
      ref, or as a Defined Term
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: a resolvable reference to a representation of a quality measure
    - $ref: '#/$defs/DefinedTerm'
  dqv:value:
    description: the reported result of the quality measure, either as a string or
      a defined term from a vocabulary
    anyOf:
    - type: string
    - $ref: '#/$defs/DefinedTerm'
required:
- dqv:isMeasurementOf
- dqv:value
$defs:
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/context.jsonld)

## Sources

* 

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/qualityProperties/qualityMeasure`

