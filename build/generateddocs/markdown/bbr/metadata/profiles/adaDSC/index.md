
# ADA DSC Profile (Schema)

`cdif.bbr.metadata.profiles.adaDSC` *v0.1*

Technique-specific profile for Differential Scanning Calorimetry (DSC) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA DSC Profile

Technique-specific metadata profile for Differential Scanning Calorimetry (DSC) products in the Astromat Data Archive. Differential scanning calorimetry thermal analysis.

## Product Types
- `ada:DSCHeatTabular`
- `ada:DSCResultsTabular`

## Valid Component Types
- `ada:DSCHeatTabular`
- `ada:DSCResultsTabular`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailDSC`

## Examples

### DSC Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:DSCHeatTabular", "ada:DataDeliveryPackage"],
  "schema:name": "DSC Analysis of Sample",
  "schema:description": "Differential Scanning Calorimetry (DSC) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA DSC Product Profile
description: Technique-specific profile for Differential Scanning Calorimetry (DSC)
  products. Extends the base ADA product profile with constraints on valid DSC component
  types and detailDSC requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a DSC product type identifier.
      contains:
        enum:
        - ada:DSCHeatTabular
        - ada:DSCResultsTabular
        - Differential Scanning Calorimetry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:DSCHeatTabular
                    - ada:DSCResultsTabular
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaDSC/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaDSC/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaDSC/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaDSC`

