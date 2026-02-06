
# Person or Organization in Role (Schema)

`cdif.bbr.metadata.schemaorgProperties.agentInRole` *v0.1*

Schema to documennt a person or organization in a role relative to some resoruce, uses schema.org/Role construct.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Person or Organization in Role properties

Defines a set of properties for use describing a role filled by a person or an organization (an 'agent') for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.  Use to relate people or organizations to resources in particular roles.  

TBD-- extension for machine agents.
## Examples

### Example organization in role.
Example role instance, organization.

In **Markdown** format.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": "schema:Role",
    "schema:roleName": "owner",
    "schema:contributor": {
        "@id": "ex:exampleOrg_fW",
        "@type": "schema:Organization",
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
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": "schema:Role",
  "schema:roleName": "owner",
  "schema:contributor": {
    "@id": "ex:exampleOrg_fW",
    "@type": "schema:Organization",
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
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:exampleOrg_fW a schema1:Organization ;
    schema1:alternateName "UAz" ;
    schema1:description "University in Tucson, Arizona" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/03m2x1q45" ;
            schema1:value "03m2x1q45" ] ;
    schema1:name "University of Arizona" ;
    schema1:sameAs "Wildcats" .

[] a schema1:Role ;
    schema1:contributor ex:exampleOrg_fW ;
    schema1:roleName "owner" .


```


### Example person in role
Example person in role instance.   
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/"
    },
    "@type": "schema:Role",
    "schema:roleName": "editor",
    "schema:contributor": {
        "@id": "ex:PersonExample_zZc",
        "@type": "schema:Person",
        "schema:name": "Joe B. Test",
        "schema:alternateName": "Test, J. B.",
        "schema:affiliation": {
            "@type": "schema:Organization",
            "schema:name": "The Big Manufacturing Co."
        },
        "schema:description": "Metadata specialist, based in Portland, Maine",
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://orcid.org",
            "schema:value": "iY",
            "schema:url": "https://orcid.org/iY"
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
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@type": "schema:Role",
  "schema:roleName": "editor",
  "schema:contributor": {
    "@id": "ex:PersonExample_zZc",
    "@type": "schema:Person",
    "schema:name": "Joe B. Test",
    "schema:alternateName": "Test, J. B.",
    "schema:affiliation": {
      "@type": "schema:Organization",
      "schema:name": "The Big Manufacturing Co."
    },
    "schema:description": "Metadata specialist, based in Portland, Maine",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://orcid.org",
      "schema:value": "iY",
      "schema:url": "https://orcid.org/iY"
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
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:PersonExample_zZc a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "The Big Manufacturing Co." ] ;
    schema1:alternateName "Test, J. B." ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@bmanuco.org" ] ;
    schema1:description "Metadata specialist, based in Portland, Maine" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/iY" ;
            schema1:value "iY" ] ;
    schema1:name "Joe B. Test" ;
    schema1:sameAs "https://ark.org/46737",
        "uri:test:43737" .

[] a schema1:Role ;
    schema1:contributor ex:PersonExample_zZc ;
    schema1:roleName "editor" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: For more granularity on how a person contributed to a Dataset, use schema:Role.
  The schema.org documentation does not state that the Role type is an expected data
  type of author, creator and contributor, but that is addressed in this blog post
  (http://blog.schema.org/2014/06/introducing-role.html). see https://github.com/ESIPFed/science-on-schema.org/blob/develop/guides/Dataset.md#roles-of-people
type: object
properties:
  '@type':
    type: string
    const: schema:Role
  schema:roleName:
    type: string
  schema:contributor:
    type: object
    oneOf:
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
    - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/context.jsonld)

## Sources

* [schema.org](https://schema.org/Role)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/schemaorgProperties/agentInRole`

