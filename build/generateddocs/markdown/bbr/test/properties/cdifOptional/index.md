
# CDIF discovery metadata, Optional elements (Schema)

`ogc.bbr.test.properties.cdifOptional` *v0.1*

Definition of optional metadata elements for CDIF discovery profile

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Base Metadata properties

Defines simple properties included in CDIF discvoery metadata for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example CDIF record
Example CDIF record with mandatory and optional properties.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:cdifOptional_23578",
    "@type": ["schema:Dataset"],
    "schema:name": "Bathymetry Bay of Biscay",
    "schema:identifier":"https://doi.org/23566/aslry",
    "schema:additionalType": [""],
    "schema:description": "description of resource",
    "schema:version": "1.0",
    "schema:url": "https://example.org/landingPage254266",
    "schema:inLanguage": "en",
    "schema:dateModified": "2022-12-12",
    "schema:datePublished": "2021-11-14",
    "schema:license": ["https://creativecommons.org/publicdomain/zero/1.0/"],
    "schema:conditionsOfAccess": [
        {
            "@id": "ex:LabeledLinkExample_qZc",
            "@type": "schema:CreativeWork",
            "schema:name": "conditions of access statement",
            "schema:description": "URL to get the document",
            "schema:url": "https://example.org/conditions/2342747"
        }
    ],
    "schema:relatedLink": [
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": "related data",
            "target": {
                "@type": "schema:EntryPoint",
                "schema:encodingFormat": "image/jpg",
                "schema:name": "Image of seafloor geology map, bay of Biscay",
                "schema:url": "https://example.org/geology/baybiscay"
            }
        }
    ],
    "schema:publishingPrinciples": ["https://example.org/principles/3478"]
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "https//schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/cdifOptional/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:cdifOptional_23578",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Bathymetry Bay of Biscay",
  "schema:identifier": "https://doi.org/23566/aslry",
  "schema:additionalType": [
    ""
  ],
  "schema:description": "description of resource",
  "schema:version": "1.0",
  "schema:url": "https://example.org/landingPage254266",
  "schema:inLanguage": "en",
  "schema:dateModified": "2022-12-12",
  "schema:datePublished": "2021-11-14",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:conditionsOfAccess": [
    {
      "@id": "ex:LabeledLinkExample_qZc",
      "@type": "schema:CreativeWork",
      "schema:name": "conditions of access statement",
      "schema:description": "URL to get the document",
      "schema:url": "https://example.org/conditions/2342747"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "related data",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:encodingFormat": "image/jpg",
        "schema:name": "Image of seafloor geology map, bay of Biscay",
        "schema:url": "https://example.org/geology/baybiscay"
      }
    }
  ],
  "schema:publishingPrinciples": [
    "https://example.org/principles/3478"
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:cdifOptional_23578 a schema1:Dataset ;
    schema1:additionalType "" ;
    schema1:conditionsOfAccess ex:LabeledLinkExample_qZc ;
    schema1:dateModified "2022-12-12" ;
    schema1:datePublished "2021-11-14" ;
    schema1:description "description of resource" ;
    schema1:identifier "https://doi.org/23566/aslry" ;
    schema1:inLanguage "en" ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:name "Bathymetry Bay of Biscay" ;
    schema1:publishingPrinciples "https://example.org/principles/3478" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "related data" ] ;
    schema1:url "https://example.org/landingPage254266" ;
    schema1:version "1.0" .

ex:LabeledLinkExample_qZc a schema1:CreativeWork ;
    schema1:description "URL to get the document" ;
    schema1:name "conditions of access statement" ;
    schema1:url "https://example.org/conditions/2342747" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: 'Optional properties for CDIF discovery metadata schema, with schema: prefixes'
description: Building block specifies properties for CDIF schama.org discovery record
properties:
  schema:description:
    type: string
    description: A short summary describing a dataset. This text will be indexed by
      search applications, so the more information here, the better.
  schema:additionalType:
    description: identifiers for datatypes from other vocabularies (not schema.org)
      that apply to this metadata.
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
  schema:sameAs:
    description: The other identifiers for the dataset. Schema.org has three ways
      of encoding identifiers-- a text description, a URL, or by using the schema:PropertyValue
      field. The Science on Schema.org guidance strongly recommends using the PropertyValue
      approach. see https://github.com/ESIPFed/science-on-schema.org   .... Dataset.md#identifier.
    type: array
    minItems: 0
    items:
      anyOf:
      - $ref: '#/$defs/Identifier'
      - type: string
  schema:version:
    type:
    - string
    - number
    description: The version number or identifier for this dataset (text or numeric).
      The values should sort from oldest to newest using an alphanumeric sort on version
      strings
  schema:inLanguage:
    type: string
    description: the language of the dataset content
  schema:datePublished:
    type: string
    description: ISO8601 formatted date (and optional time if relevant) when Dataset
      was made public.
  schema:relatedLink:
    type: array
    description: links to related resources; linkRelationship specifies how the resource
      is related.
    items:
      type: object
      properties:
        '@type':
          type: string
          const: schema:LinkRole
        schema:linkRelationship:
          anyOf:
          - $ref: '#/$defs/DefinedTerm'
          - type: string
        target:
          type: object
          properties:
            '@type':
              type: string
              const: schema:EntryPoint
            schema:encodingFormat:
              type: string
              description: registered MIME types are expected
            schema:name:
              type: string
            schema:url:
              type: string
              format: uri
  schema:publishingPrinciples:
    description: FDOF digitalObjectMutability, RDA digitalObjectPolicy, FDOF PersistencyPolicy.
      Policies related to maintenance, update, expected time to live. If an online
      resource documents the policies or a URI is used to identify the conditions,
      recommend using schema:CreativeWork to provide a label (name) and an identifier
      (URI or URL).
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: a reference to a publishing principles statement
      - $ref: '#/$defs/LabeledLink'
  schema:keywords:
    description: Keywords are an array of strings, an array of schema:DefinedTerms,
      or some combination of these. If you have information about a controlled vocabulary
      from which keywords come from, use schema:DefinedTerm to descibe that keyword.
      This allowed variability makes parsing metadata hard; recommend using DefinedTerm
      for all keywords if any of them are from a known vocabulary, otherwise an array
      of strings.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DefinedTerm'
      - type: string
  schema:creator:
    description: author or orginator of intellectual content of dataset. Uset the
      JSON-LD @list construct to preserve author order. Use contributor with the Role
      property to specify other roles related to creation or stewardship of the resource.
    type: object
    properties:
      '@list':
        type: array
        items:
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
                description: a identifier for an agent defined in this metadata, or
                  externally; must be dereferenceable
          - $ref: '#/$defs/Person'
          - $ref: '#/$defs/Organization'
  schema:contributor:
    description: other parties who played a role in production of dataset
    type: array
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
            description: a identifier for an agent defined in this metadata, or externally;
              must be dereferenceable
      - $ref: '#/$defs/Person'
      - $ref: '#/$defs/Organization'
      - $ref: '#/$defs/Contributor'
  schema:publisher:
    description: Party who made the dataset publicly available
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
          description: a identifier for an agent defined in this metadata, or externally;
            must be dereferenceable
    - $ref: '#/$defs/Person'
    - $ref: '#/$defs/Organization'
  schema:provider:
    description: Party who maintains the distribution options for the dataset. If
      there are multiple distributions from different providers, use the provider
      property on distribution/DataDownload
    type: array
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
            description: a identifier for an agent defined in this metadata, or externally;
              must be dereferenceable
      - $ref: '#/$defs/Person'
      - $ref: '#/$defs/Organization'
  schema:funding:
    type: array
    items:
      $ref: '#/$defs/Funder'
  schema:variableMeasured:
    description: What does the dataset measure? (e.g., temperature, pressure)
    type: array
    items:
      $ref: '#/$defs/VariableMeasured'
  schema:spatialCoverage:
    description: To specify location that is the subject of resource content; use
      schema.org place names, bounding box, point or optional OGC WKT gemetry.
    type: array
    items:
      $ref: '#/$defs/SpatialExtent'
  schema:temporalCoverage:
    description: The time interval during which data was collected or observations
      were made; or a time period that an activity or collection is linked to intellectually
      or thematically (for example, 1997 to 1998; the 18th century) (see https://documentation.ardc.edu.au/display/DOC/Temporal+coverage).
      For documentation of Earth Science, Paleobiology or Paleontology datasets, we
      are interested in the second case-- the time period that data are linked to
      thematically..
    type: array
    items:
      $ref: '#/$defs/TemporalExtent'
$defs:
  LabeledLink:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/labeledLink/schema.yaml
  Identifier:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml
  DefinedTerm:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.yaml
  Person:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/person/schema.yaml
  Organization:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/schema.yaml
  Contributor:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/agentInRole/schema.yaml
  Funder:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/funder/schema.yaml
  VariableMeasured:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/variableMeasured/schema.yaml
  SpatialExtent:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/temporalExtent/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/cdifOptional/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/cdifOptional/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/cdifOptional/context.jsonld)

## Sources

* [schema.org](https://schema.org/Dataset)
* [Cross Domain Interoperability Framework Discovery Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/discovery.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/cdifOptional`

