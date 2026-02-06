
# ADA VNMIR Profile (Schema)

`cdif.bbr.metadata.profiles.adaVNMIR` *v0.1*

Technique-specific profile for Very-Near Mid-Infrared (VNMIR/FTIR) spectroscopy products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA VNMIR Profile

Technique-specific metadata profile for Very-Near Mid-Infrared (VNMIR) and FTIR spectroscopy products in the Astromat Data Archive. VNMIR/FTIR measures the infrared absorption and emission of materials to determine molecular composition and structure, used extensively for mineral identification in planetary and terrestrial samples.

## Product Types
- **VNMIR Point** - Single-point spectral measurements
- **VNMIR Overview Image** - Overview image maps with spectral registration
- **VNMIR Spectral Map** - Hyperspectral data cubes

## Valid Component Types
- `ada:VNMIRSpectralPoint` - Point spectral measurements in tabular format (vnmir_detail)
- `ada:VNMIROverviewImage` - Overview image maps with spectral context (vnmir_detail)
- `ada:VNMIRSpectralMap` - Hyperspectral data cubes (vnmir_detail)
- `ada:VNMIRSpectraPlot` - Spectral plot images or documents
- `ada:analysisLocation` - Analysis location images
- `ada:instrumentMetadata` - Instrument metadata documents
- `ada:methodDescription` - Method description documents

## Detail Type
`vnmir_detail` with 20+ properties including: `detector`, `beamsplitter`, `calibrationStandards`, `comments`, `numberOfScans`, `eMaxFitRegionMin/Max`, `emissionAngle`, `emissivityMaximum`, `environmentalPressure`, `incidenceAngle`, `measurement`, `measurementEnvironment`, `phaseAngle`, `sampleHeated`, `samplePreparation`, `sampleTemperature`, `spectralRangeMin/Max`, `spectralResolution`, `spectralSampling`, `spotSize`, `uncertaintyNoise`, `vacuumExposedSample`

## Examples

### VNMIR Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:VNMIRPoint", "ada:DataDeliveryPackage"],
  "schema:name": "VNMIR Spectral Analysis of Mineral",
  "schema:description": "Very-near mid-infrared spectroscopy data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVNMIR/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:VNMIRPoint",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "VNMIR Spectral Analysis of Mineral",
  "schema:description": "Very-near mid-infrared spectroscopy data"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "ada:DataDeliveryPackage",
        "ada:VNMIRPoint" ;
    schema1:description "Very-near mid-infrared spectroscopy data" ;
    schema1:name "VNMIR Spectral Analysis of Mineral" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA VNMIR Product Profile
description: Technique-specific profile for Very-Near Mid-Infrared (VNMIR/FTIR) spectroscopy
  products. Extends the base ADA product profile with constraints on valid VNMIR component
  types and vnmir_detail requirements.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a VNMIR product type identifier.
      contains:
        enum:
        - ada:VNMIRPoint
        - ada:VNMIROverviewImage
        - ada:VNMIRSpectralMap
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:VNMIRSpectralPoint
                    - ada:VNMIROverviewImage
                    - ada:VNMIRSpectralMap
                    - ada:VNMIRSpectraPlot
                    - ada:analysisLocation
                    - ada:instrumentMetadata
                    - ada:methodDescription
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVNMIR/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVNMIR/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaVNMIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaVNMIR`

