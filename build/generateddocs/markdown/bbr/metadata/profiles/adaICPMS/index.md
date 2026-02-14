
# ADA ICP-MS Profile (Schema)

`cdif.bbr.metadata.profiles.adaICPMS` *v0.1*

Technique-specific profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA ICP-MS Profile

Technique-specific metadata profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products in the Astromat Data Archive. ICP-MS measures elemental and isotopic concentrations by ionizing samples in an argon plasma and separating ions by mass-to-charge ratio. This profile covers HR-ICP-MS (high resolution), Q-ICP-MS (quadrupole), and MC-ICP-MS (multi-collector) variants.

## Product Types
- **HR-ICP-MS Processed/Raw** - High-resolution ICP-MS data
- **Q-ICP-MS Processed/Raw** - Quadrupole ICP-MS data
- **MC-ICP-MS Raw/Processed** - Multi-collector ICP-MS data

## Valid Component Types
- `ada:HRICPMSProcessed` - HR-ICP-MS processed tabular data
- `ada:HRICPMSRaw` - HR-ICP-MS raw tabular data or documents
- `ada:QICPMSProcessedTabular` - Q-ICP-MS processed tabular data
- `ada:QICPMSRawTabular` - Q-ICP-MS raw tabular data
- `ada:MCICPMSTabular` - MC-ICP-MS tabular data
- `ada:MCICPMSCollection` - MC-ICP-MS data collections
- `ada:MCICPMSRaw` - MC-ICP-MS raw documents (e.g., Neptune Plus .exp files)
- `ada:methodDescription` - Method description documents
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:calibrationFile` - Calibration documents

## Detail Type
No ICP-MS-specific detail type; component types are enum-only.

## Examples

### ICP-MS Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:HRICPMSProcessed", "ada:DataDeliveryPackage"],
  "schema:name": "HR-ICP-MS Elemental Analysis",
  "schema:description": "High-resolution ICP-MS elemental concentration data"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA ICP-MS Product Profile
description: Technique-specific profile for Inductively Coupled Plasma Mass Spectrometry
  (ICP-MS) products. Covers HR-ICP-MS, Q-ICP-MS, and MC-ICP-MS variants. Extends the
  base ADA product profile with constraints on valid ICP-MS component types.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include an ICP-MS product type identifier.
      contains:
        enum:
        - ada:HRICPMSProcessed
        - ada:HRICPMSRaw
        - ada:QICPMSProcessed
        - ada:QICPMSRaw
        - ada:MCICPMSRaw
        - ada:MCICPMSProcessed
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:HRICPMSProcessed
                    - ada:HRICPMSRaw
                    - ada:QICPMSProcessedTabular
                    - ada:QICPMSRawTabular
                    - ada:MCICPMSTabular
                    - ada:MCICPMSCollection
                    - ada:MCICPMSRaw
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

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPMS/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/adaICPMS/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/_sources/profiles/adaICPMS/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/adaICPMS`

