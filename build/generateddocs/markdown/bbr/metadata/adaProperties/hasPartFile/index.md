
# Has Part File Type (Schema)

`cdif.bbr.metadata.adaProperties.hasPartFile` *v0.1*

Files within archive distribution, extends files type

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Has Part File Type

Describes files within an archive distribution (e.g., files inside a zip archive). Reuses the files type schema for describing individual files within a `schema:hasPart` array of a `schema:DataDownload` distribution.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Has Part File Type
description: Describes files within an archive distribution (e.g., files inside a
  zip archive). Extends the files type pattern for use within schema:hasPart arrays.
$ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/files/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/hasPartFile/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/hasPartFile`

