
# Metadata Conforms to for XAS (Schema)

`cdif.bbr.metadata.xasProperties.xasSubject` *v0.1*

For XAS profle, need to declare conformatnce iwht provile in the metadata

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Metadata metadata for XAS profile properties

Only addition is declaration of conformance.
## Examples

### Example XAS metadata conforms to extension.
Import base schema.org SubjectOf, add requiremnet that dcterms:conformsTo has XAS profile URI.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/"
    },
    "@id": "ex:subject-pz63",
    "@type": "schema:Dataset",
    "schema:dateModified": "2025-08-26",
    "schema:creator": [
        {
            "@id": "https://ada.org/person/3479",
            "@type": "schema:Person",
            "schema:name": "Richard, Stephen M.",
            "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "smrTucson@email.org"
            }
        }
    ],
    "schema:about": {"@id": "xas:485749"},
    "schema:description": "metadata about documentation for se_na2so4",
    "dcterms:conformsTo": [
        {"@id": "cdif:profile_basic_1.0"},
        {"@id": "cdif:profile_xasCDIF"}
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
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasSubject/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/"
    }
  ],
  "@id": "ex:subject-pz63",
  "@type": "schema:Dataset",
  "schema:dateModified": "2025-08-26",
  "schema:creator": [
    {
      "@id": "https://ada.org/person/3479",
      "@type": "schema:Person",
      "schema:name": "Richard, Stephen M.",
      "schema:identifier": "https://orcid.org/0000-0002-7933-2154",
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "smrTucson@email.org"
      }
    }
  ],
  "schema:about": {
    "@id": "xas:485749"
  },
  "schema:description": "metadata about documentation for se_na2so4",
  "dcterms:conformsTo": [
    {
      "@id": "cdif:profile_basic_1.0"
    },
    {
      "@id": "cdif:profile_xasCDIF"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .

ex:subject-pz63 a schema1:Dataset ;
    dcterms:conformsTo <cdif:profile_basic_1.0>,
        <cdif:profile_xasCDIF> ;
    schema1:about xas:485749 ;
    schema1:creator <https://ada.org/person/3479> ;
    schema1:dateModified "2025-08-26" ;
    schema1:description "metadata about documentation for se_na2so4" .

<https://ada.org/person/3479> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "smrTucson@email.org" ] ;
    schema1:identifier "https://orcid.org/0000-0002-7933-2154" ;
    schema1:name "Richard, Stephen M." .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/metaMetadata/schema.yaml
- properties:
    dcterms:conformsTo:
      type: array
      items:
        $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/metaMetadata/schema.yaml#/$defs/conformsTo_item
      minItems: 2
      contains:
        type: object
        properties:
          '@id':
            const: cdif:profile_xasCDIF
        required:
        - '@id'
      minContains: 1
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasSubject/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasSubject/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "https://schema.org",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasSubject/context.jsonld)

## Sources

* 

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/xasProperties/xasSubject`

