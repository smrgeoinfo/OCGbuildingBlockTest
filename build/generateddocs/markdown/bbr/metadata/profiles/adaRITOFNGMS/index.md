
# ADA RI-TOF-NGMS Profile (Schema)

`cdif.bbr.metadata.profiles.adaRITOFNGMS` *v0.1*

Technique-specific profile for Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA RI-TOF-NGMS Profile

Technique-specific metadata profile for Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS) products in the Astromat Data Archive. Resonance ionization time-of-flight noble gas mass spectrometry.

## Product Types
- `ada:RITOFNGMSTabular`
- `ada:RITOFNGMSCollection`

## Valid Component Types
- `ada:RITOFNGMSTabular`
- `ada:RITOFNGMSCollection`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### RI-TOF-NGMS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:RITOFNGMSTabular", "ada:DataDeliveryPackage"],
  "schema:name": "RI-TOF-NGMS Analysis of Sample",
  "schema:description": "Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS) data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA RI-TOF-NGMS Product Profile
description: Technique-specific profile for Resonance Ionization Time-of-Flight Noble
  Gas Mass Spectrometry (RI-TOF-NGMS) products. Extends the base ADA product profile
  with constraints on valid RI-TOF-NGMS component types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a RI-TOF-NGMS product type identifier.
      contains:
        enum:
        - ada:RITOFNGMSTabular
        - ada:RITOFNGMSCollection
        - Resonance ionization time of flight noble gas mass spectrometry
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:RITOFNGMSTabular
                    - ada:RITOFNGMSCollection
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaRITOFNGMS/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaRITOFNGMS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/profiles/adaRITOFNGMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaRITOFNGMS`

