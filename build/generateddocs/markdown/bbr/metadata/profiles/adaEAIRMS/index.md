
# ADA EA-IRMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaEAIRMS` *v0.1*

Technique-specific profile for Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA EA-IRMS Profile

Technique-specific metadata profile for Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS) products in the Astromat Data Archive. Elemental analysis coupled with isotope ratio mass spectrometry.

## Product Types
- `ada:EAIRMSCollection`

## Valid Component Types
- `ada:EAIRMSCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Detail Type
`detailEAIRMS`

## Examples

### EA-IRMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:EAIRMSCollection", "ada:DataDeliveryPackage"],
  "schema:name": "EA-IRMS Analysis of Sample",
  "schema:description": "Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA EA-IRMS Product Profile
description: Technique-specific profile for Elemental Analysis - Isotope Ratio Mass
  Spectrometry (EA-IRMS) products. Extends the base ADA product profile with constraints
  on valid EA-IRMS component types and detailEAIRMS requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a EA-IRMS product type identifier.
      contains:
        enum:
        - ada:EAIRMSCollection
        - Elemental analysis - isotope ratio mass spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:EAIRMSCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaEAIRMS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaEAIRMS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaEAIRMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaEAIRMS`

