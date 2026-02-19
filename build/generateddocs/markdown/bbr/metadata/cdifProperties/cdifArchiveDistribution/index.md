
# CDIF Archive Distribution (Schema)

`cdif.bbr.metadata.cdifProperties.cdifArchiveDistribution` *v0.1*

Schema for a DataDownload distribution that is an archive containing multiple component files described via schema:hasPart, with optional CDIF data description extensions

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Defines the structure for a DataDownload distribution that is an archive file (e.g. ZIP, tar.gz) containing multiple component files. The archive itself is typed as `schema:DataDownload` with standard properties (name, contentUrl, encodingFormat, checksum). Component files within the archive are listed in `schema:hasPart` and typed as `schema:MediaObject` (not `schema:DataDownload`, since they are not independently accessible via URL).

Each hasPart item has:
- `@id` — identifier for cross-references (e.g. from metadata sidecar files via `schema:about`)
- `@type` — must include `schema:MediaObject`, must not include `schema:DataDownload`
- `schema:name` — filename within the archive
- `schema:encodingFormat` — MIME type(s)
- `schema:size` — file size as `schema:QuantitativeValue`
- `schema:description` — description of file content
- `schema:about` — references to related files (for metadata sidecars)
- `spdx:checksum` — integrity checksum

Component files may optionally include CDIF data description extensions to describe their internal data structure:
- `cdifTabularData` — for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
- `cdifDataCube` — for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Archive Distribution
description: A DataDownload distribution that is an archive file (e.g. ZIP) containing
  multiple component files described in schema:hasPart. The archive itself is typed
  as schema:DataDownload; each component file is typed as schema:MediaObject (not
  DataDownload, since they are not independently accessible via URL). Components may
  optionally include CDIF data description extensions (cdifTabularData, cdifDataCube)
  to describe their internal data structure.
type: object
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
- type: object
  properties:
    schema:hasPart:
      type: array
      description: Array describing the files contained in the archive. Each item
        represents a component file that is part of the archive and is not independently
        accessible.
      items:
        allOf:
        - type: object
          properties:
            '@id':
              type: string
              description: Identifier for this file, typically a hash-based anchor
                (e.g. '#abc123'). Used for cross-references from schema:about in metadata
                sidecar files.
            '@type':
              type: array
              description: Must include schema:MediaObject. Must NOT include schema:DataDownload
                since this file is not independently accessible. May include additional
                types for categorization.
              items:
                type: string
              contains:
                const: schema:MediaObject
              not:
                contains:
                  const: schema:DataDownload
              minItems: 1
            schema:name:
              type: string
              description: Filename of the component file within the archive.
            schema:description:
              type: string
              description: Description of the file content. May include checksum information.
            schema:encodingFormat:
              type: array
              description: MIME type(s) for this file.
              items:
                type: string
            schema:size:
              type: object
              description: File size as a QuantitativeValue.
              properties:
                '@type':
                  type: string
                  const: schema:QuantitativeValue
                schema:value:
                  type: number
                  description: Numeric size value.
                schema:unitText:
                  type: string
                  description: Unit of measure for size (e.g. 'byte').
            schema:about:
              type: array
              description: For metadata sidecar files, references the data file this
                metadata describes.
              items:
                type: object
                properties:
                  '@id':
                    type: string
                    description: Reference to the @id of the data file described by
                      this sidecar.
            spdx:checksum:
              type: object
              description: Checksum for integrity verification of this component file.
              properties:
                spdx:algorithm:
                  type: string
                spdx:checksumValue:
                  type: string
          required:
          - '@type'
          - schema:name
          - schema:encodingFormat
        - anyOf:
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
          - {}
x-jsonld-prefixes:
  schema: http://schema.org/
  spdx: http://spdx.org/rdf/terms#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)
* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifArchiveDistribution`

