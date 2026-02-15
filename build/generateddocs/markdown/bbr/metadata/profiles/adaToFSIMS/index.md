
# ADA ToF-SIMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaToFSIMS` *v0.1*

Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ToF-SIMS Profile

Technique-specific metadata profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products in the Astromat Data Archive. Time-of-flight secondary ion mass spectrometry surface analysis.

## Product Types
- `ada:TOFSIMSCollection`

## Valid Component Types
- `ada:TOFSIMSCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### ToF-SIMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:TOFSIMSCollection", "ada:DataDeliveryPackage"],
  "schema:name": "ToF-SIMS Analysis of Sample",
  "schema:description": "Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ToF-SIMS Product Profile
description: Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry
  (ToF-SIMS) products. Extends the base ADA product profile with constraints on valid
  ToF-SIMS component types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a ToF-SIMS product type identifier.
      contains:
        enum:
        - ada:TOFSIMSCollection
        - Time-of-Flight Secondary Ion Mass Spectrometer
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:TOFSIMSCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaToFSIMS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaToFSIMS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaToFSIMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaToFSIMS`

