
# Data structure description for HDF5 NEXUS files (Schema)

`cdif.bbr.metadata.xasProperties.xasHDF5DataStructure` *v0.1*

Schema defining properties to describe data structure in an HDF5 file, for use with CDIF x-ray absorption spectroscopy profile

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## XAS HDF5 data structure properties

Defines a set of properties for use describing a DataDownload in HDF5 format as a distribution for a resource. For use in the XAS  profile. 

## Examples

### Example data dowload description.
Defintion of properties to describe file-based distribution of a resource on the Web.

In **Markdown** format.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@type": ["schema:DataDownload"],
    "schema:name": "Water levels in Beartooth reservoir, 1992-2020",
    "schema:contentUrl": "https://hounddata.org/354277.csv",
    "schema:encodingFormat": ["text/csv"],
    "spdx:checksum": {
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "35247-39u83-7ik"
    },
    "schema:provider": [
        {
            "@id": "https://orcid.org/3333-4444-5565",
            "@type": "schema:Person",
            "schema:name": "Severus Data",
            "schema:alternateName": "the datameister",
            "schema:affiliation": {
                "@id": "https://ror.org/347237",
                "@type": "schema:Organization",
                "schema:additionalType": ["Data repository"],
                "schema:name": "Houndstooth Data Repository",
                "schema:identifier": "https://ror.org/347237"
            },
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "joe@email.org"
            },
            "schema:description": "Earth Science Data Custodian",
            "schema:identifier": {
                "@type": "schema:PropertyValue",
                "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
                "schema:value": "3333-4444-5565",
                "schema:url": "https://orcid.org/3333-4444-5565"
            }
        }
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
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasHDF5DataStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Water levels in Beartooth reservoir, 1992-2020",
  "schema:contentUrl": "https://hounddata.org/354277.csv",
  "schema:encodingFormat": [
    "text/csv"
  ],
  "spdx:checksum": {
    "spdx:algorithm": "MD5",
    "spdx:checksumValue": "35247-39u83-7ik"
  },
  "schema:provider": [
    {
      "@id": "https://orcid.org/3333-4444-5565",
      "@type": "schema:Person",
      "schema:name": "Severus Data",
      "schema:alternateName": "the datameister",
      "schema:affiliation": {
        "@id": "https://ror.org/347237",
        "@type": "schema:Organization",
        "schema:additionalType": [
          "Data repository"
        ],
        "schema:name": "Houndstooth Data Repository",
        "schema:identifier": "https://ror.org/347237"
      },
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "joe@email.org"
      },
      "schema:description": "Earth Science Data Custodian",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:value": "3333-4444-5565",
        "schema:url": "https://orcid.org/3333-4444-5565"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix ns1: <spdx:> .
@prefix schema1: <http://schema.org/> .

<https://orcid.org/3333-4444-5565> a schema1:Person ;
    schema1:affiliation <https://ror.org/347237> ;
    schema1:alternateName "the datameister" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@email.org" ] ;
    schema1:description "Earth Science Data Custodian" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
            schema1:url "https://orcid.org/3333-4444-5565" ;
            schema1:value "3333-4444-5565" ] ;
    schema1:name "Severus Data" .

<https://ror.org/347237> a schema1:Organization ;
    schema1:additionalType "Data repository" ;
    schema1:identifier "https://ror.org/347237" ;
    schema1:name "Houndstooth Data Repository" .

[] a schema1:DataDownload ;
    schema1:contentUrl "https://hounddata.org/354277.csv" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "Water levels in Beartooth reservoir, 1992-2020" ;
    schema1:provider <https://orcid.org/3333-4444-5565> ;
    ns1:checksum [ ns1:algorithm "MD5" ;
            ns1:checksumValue "35247-39u83-7ik" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema to document file-based access to a resoruce via URL, based on
  schema.org/DataDownload
type: object
properties:
  '@id':
    type: string
  '@type':
    type: array
    description: implement as array because extensions might need to add additional
      types
    items:
      type: string
    contains:
      const: schema:DataDownload
    minItems: 1
  schema:name:
    type: string
  schema:contentUrl:
    type: string
    format: uri
  schema:encodingFormat:
    type: array
    items:
      type: string
  spdx:checksum:
    type: object
    description: A string value calculated from the content of the resource representation,
      used to test if content has been modified. The checksum is a property of a particular
      distribution/DataDownload.
    properties:
      spdx:algorithm:
        type: string
      spdx:checksumValue:
        type: string
  schema:provider:
    type: array
    description: Party who maintains this particular distribution option for the dataset.
      Use this property if there are multiple distributions from different providers
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
      - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
      - $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
required:
- schema:contentUrl
- '@type'
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasHDF5DataStructure/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasHDF5DataStructure/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasHDF5DataStructure/context.jsonld)

## Sources

* 

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/xasProperties/xasHDF5DataStructure`

