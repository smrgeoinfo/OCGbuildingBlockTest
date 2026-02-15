
# ADA SV-RUEC Profile (Schema)

`cdif.bbr.metadata.profiles.adaSVRUEC` *v0.1*

Technique-specific profile for Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA SV-RUEC Profile

Technique-specific metadata profile for Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) products in the Astromat Data Archive. Seismic velocities and rock ultrasonic elastic constants measurement.

## Product Types
- `ada:SVRUECTabular`

## Valid Component Types
- `ada:SVRUECTabular`
- `ada:analysisLocation`
- `ada:methodDescription`
- `ada:instrumentMetadata`
- `ada:calibrationFile`

## Examples

### SV-RUEC Product Example
#### json
```json
{
  "@type": ["schema:Dataset", "schema:Product"],
  "schema:additionalType": ["ada:SVRUECTabular", "ada:DataDeliveryPackage"],
  "schema:name": "SV-RUEC Analysis of Sample",
  "schema:description": "Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) data"
}

```

#### jsonld
```jsonld
{
  "@context": "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaSVRUEC/context.jsonld",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:additionalType": [
    "ada:SVRUECTabular",
    "ada:DataDeliveryPackage"
  ],
  "schema:name": "SV-RUEC Analysis of Sample",
  "schema:description": "Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) data"
}
```

#### ttl
```ttl
@prefix ns1: <schema:> .

[] a ns1:Dataset,
        ns1:Product ;
    ns1:additionalType "ada:DataDeliveryPackage",
        "ada:SVRUECTabular" ;
    ns1:description "Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) data" ;
    ns1:name "SV-RUEC Analysis of Sample" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA SV-RUEC Product Profile
description: Technique-specific profile for Seismic Velocities and Rock Ultrasonic
  Elastic Constants (SV-RUEC) products. Extends the base ADA product profile with
  constraints on valid SV-RUEC component types.
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include a SV-RUEC product type identifier.
      contains:
        enum:
        - ada:SVRUECTabular
        - Seismic Velocities and Rock Ultrasonic Elastic Constants
    schema:distribution:
      items:
        properties:
          schema:hasPart:
            items:
              properties:
                schema:additionalType:
                  items:
                    enum:
                    - ada:SVRUECTabular
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

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaSVRUEC/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaSVRUEC/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "https://schema.org",
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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/profiles/adaSVRUEC/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/profiles/adaSVRUEC`

