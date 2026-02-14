
# ADA RAMAN Profile (Schema)

`cdif.bbr.metadata.profiles.adaRAMAN` *v0.1*

Technique-specific profile for Raman Spectroscopy (RAMAN) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA RAMAN Profile

Technique-specific metadata profile for Raman Spectroscopy (RAMAN) products in the Astromat Data Archive. Raman spectroscopy vibrational analysis.

## Product Types
- `ada:RAMANRawTabular`

## Valid Component Types
- `ada:RAMANRawTabular`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### RAMAN Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:RAMANRawTabular", "ada:DataDeliveryPackage"],
  "schema:name": "RAMAN Analysis of Sample",
  "schema:description": "Raman Spectroscopy (RAMAN) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA RAMAN Product Profile
description: Technique-specific profile for Raman Spectroscopy (RAMAN) products. Extends
  the base ADA product profile with constraints on valid RAMAN component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a RAMAN product type identifier.
      contains:
        enum:
        - ada:RAMANRawTabular
        - Raman vibrational spectroscopy
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:RAMANRawTabular
                    - ada:analysisLocation
                    - ada:methodDescription
                    - ada:instrumentMetadata
                    - ada:calibrationFile
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  nxs: http://purl.org/nexusformat/definitions/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaRAMAN/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaRAMAN/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/_sources/profiles/adaRAMAN/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaRAMAN`

