
# Organization (Schema)

`ogc.bbr.test.properties.organization` *v0.1*

Schema defining propertis of an organization in CDIF context. Implementation is a profile of schema.org/Organization.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Organization properties

Defines a set of properties for use describing a organization for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example organization.
Example organization instance.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:exampleOrg_fW",
    "@type": "schema:Organization",
    "schema:additionalType": [
        "schema:ResearchOrganization",
        "university"
    ],
    "schema:name": "University of Arizona",
    "schema:alternateName": "UAz",
    "schema:description": "University in Tucson, Arizona",
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://registry.identifiers.org/registry/ror",
        "schema:value": "03m2x1q45",
        "schema:url": "https://ror.org/03m2x1q45"
    },
    "schema:sameAs": ["Wildcats"]
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:exampleOrg_fW",
  "@type": "schema:Organization",
  "schema:additionalType": [
    "schema:ResearchOrganization",
    "university"
  ],
  "schema:name": "University of Arizona",
  "schema:alternateName": "UAz",
  "schema:description": "University in Tucson, Arizona",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/ror",
    "schema:value": "03m2x1q45",
    "schema:url": "https://ror.org/03m2x1q45"
  },
  "schema:sameAs": [
    "Wildcats"
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:exampleOrg_fW a schema1:Organization ;
    schema1:additionalType "schema:ResearchOrganization",
        "university" ;
    schema1:alternateName "UAz" ;
    schema1:description "University in Tucson, Arizona" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/03m2x1q45" ;
            schema1:value "03m2x1q45" ] ;
    schema1:name "University of Arizona" ;
    schema1:sameAs "Wildcats" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  '@id':
    type: string
  '@type':
    type: string
    const: schema:Organization
    default: schema:Organization
  schema:additionalType:
    type: array
    items:
      anyOf:
      - type: string
        enum:
        - schema:FundingAgency
        - schema:Consortium
        - schema:Corporation
        - schema:EducationalOrganization
        - schema:FundingScheme
        - schema:GovernmentOrganization
        - schema:NGO
        - schema:Project
        - schema:ResearchOrganization
      - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/definedTerm/schema.yaml
      - type: string
  schema:name:
    type: string
    description: string label for organization that is meaningful for human users
  schema:alternateName:
    type: string
    description: other labels by which the organization might be known
  schema:description:
    type: string
  schema:identifier:
    description: identifier for organization
    anyOf:
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/identifier/schema.yaml
    - type: string
  schema:sameAs:
    type: array
    description: other identifiers for the organization
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/test/properties/organization/context.jsonld)

## Sources

* [schema.org](https://schema.org/Organization)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/properties/organization`

