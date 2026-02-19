
# CDIF complete metadata (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFcomplete` *v0.1*

Profile combining CDIF discovery metadata with data description extensions for distributions (single-file, archive with hasPart, and WebAPI) and optional tabular/dataCube physical mappings

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF complete metadata properties

Profile assembling building blocks for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) complete profile. Extends the CDIFDiscovery profile with data description and archive distribution extensions.

### Composition

- **CDIFDiscovery** — mandatory and optional discovery metadata (cdifMandatory + cdifOptional), including variableMeasured descriptions
- **Data description extensions** — distribution items may include CDIF data description properties:
  - `cdifTabularData` — for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
  - `cdifDataCube` — for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings
- **Archive distribution** (`cdifArchiveDistribution`) — for archive files (ZIP, tar.gz) containing multiple component files described via `schema:hasPart`, each typed as `schema:MediaObject` with optional data description extensions
- **WebAPI distribution** — for API-based data access with `schema:potentialAction` describing query endpoints and result data descriptions

### Distribution types

Each `schema:distribution` item must match one of:

1. **Single-file DataDownload** — a directly accessible file with optional tabular/dataCube data description
2. **Archive DataDownload** — an archive file with `schema:hasPart` listing component files
3. **WebAPI** — an API endpoint with `schema:potentialAction` describing available queries and their result format

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF complete metadata schema
description: JSON schema for JSON-LD documents that describe science datasets for
  the CDIF complete profile, combining discovery metadata with data description and
  archive distribution extensions. Extends CDIFDiscovery (cdifMandatory + cdifOptional
  including variableMeasured) with distribution constraints supporting single-file
  DataDownloads with optional tabular/dataCube data description, archive distributions
  with hasPart component files, and WebAPI distributions with potentialAction result
  data description.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDiscovery/schema.yaml
- type: object
  properties:
    schema:distribution:
      type: array
      items:
        anyOf:
        - allOf:
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
          - anyOf:
            - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
            - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
            - {}
        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml
        - allOf:
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/webAPI/schema.yaml
          - type: object
            properties:
              schema:potentialAction:
                type: array
                items:
                  type: object
                  properties:
                    schema:result:
                      allOf:
                      - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
                      - anyOf:
                        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
                        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
                        - {}
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)
* [schema.org DataDownload](https://schema.org/DataDownload)
* [schema.org WebAPI](https://schema.org/WebAPI)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFcomplete`

