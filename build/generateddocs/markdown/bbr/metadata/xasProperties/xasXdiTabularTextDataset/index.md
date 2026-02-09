
# XDI data structure description (Schema)

`cdif.bbr.metadata.xasProperties.xasXdiTabularTextDataset` *v0.1*

Schema defining properties to describe the structure of an XDI file. This is a fixed-wide tabular text data structure for describing the result of x-ray absorption spectroscopy experiments.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## XDI format tabular text data structure properties

Defintion of properties to describe structure of tabular data formatted following the xdi specification.  This is a very simplified description for tabular text data with fixed width columns. TBD--generalize for generic delimited tabular text formats, based on CSV for the web, Croissant, other applicable specifications.[Format specification](https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md)
## Examples

### Example XDI-format data download for simple tabular text description.
Defintion of properties to describe structure of tabular data formatted following the xdi specification.  This is a very simplified description for tabular text data with fixed width columns. TBD--generalize for generic delimited tabular text formats, based on CSV for the web, Croissant, other applicable specifications.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "xas": "https://xas.org/dictionary/"
    },
    "@id": "ex:xasXDIdownload_23463h",
    "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataset"
    ],
    "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
    "schema:description": "Distribution = PhysicalDataSet text file conformant with XDI specification",
    "schema:contentSize": "30 kb",
    "schema:encodingFormat": ["text/plain"],
    "dcterms:conformsTo": ["https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"],
    "cdi:allowsDuplicates": false,
    "cdi:has_TextMapping": [
        {
            "@type": "cdi:TextMapping",
            "cdi:formats": {"@id": "xas:monochromatorEnergyVariable"},
            "cdi:label": "energy",
            "cdi:hasRole": "Dimension",
            "cdi:index": 1,
            "cdi:length": 12
        },
        {
            "@type": "cdi:TextMapping",
            "cdi:formats": {"@id": "xas:incidentIntensityVariable"},
            "cdi:label": "i0",
            "cdi:hasRole": "Measure",
            "index": 3,
            "length": 13
        },
        {
            "@type": "cdi:TextMapping",
            "cdi:formats": {"@id": "xas:transmittedIntensityVariable"},
            "cdi:label": "it",
            "cdi:hasRole": "Measure",
            "cdi:index": 2,
            "cdi:length": 12
        }
    ],
    "allowsDuplicates": false,
    "arrayBase": 1,
    "commentPrefix": "#",
    "hasHeader": true,
    "headerRowCount": 27,
    "skipInitialSpace": true,
    "isDelimited": false,
    "isFixedWidth": true
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org"
    },
    "https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "xas": "https://xas.org/dictionary/"
    }
  ],
  "@id": "ex:xasXDIdownload_23463h",
  "@type": [
    "schema:DataDownload",
    "cdi:TabularTextDataset"
  ],
  "schema:contentUrl": "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi",
  "schema:description": "Distribution = PhysicalDataSet text file conformant with XDI specification",
  "schema:contentSize": "30 kb",
  "schema:encodingFormat": [
    "text/plain"
  ],
  "dcterms:conformsTo": [
    "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
  ],
  "cdi:allowsDuplicates": false,
  "cdi:has_TextMapping": [
    {
      "@type": "cdi:TextMapping",
      "cdi:formats": {
        "@id": "xas:monochromatorEnergyVariable"
      },
      "cdi:label": "energy",
      "cdi:hasRole": "Dimension",
      "cdi:index": 1,
      "cdi:length": 12
    },
    {
      "@type": "cdi:TextMapping",
      "cdi:formats": {
        "@id": "xas:incidentIntensityVariable"
      },
      "cdi:label": "i0",
      "cdi:hasRole": "Measure",
      "index": 3,
      "length": 13
    },
    {
      "@type": "cdi:TextMapping",
      "cdi:formats": {
        "@id": "xas:transmittedIntensityVariable"
      },
      "cdi:label": "it",
      "cdi:hasRole": "Measure",
      "cdi:index": 2,
      "cdi:length": 12
    }
  ],
  "allowsDuplicates": false,
  "arrayBase": 1,
  "commentPrefix": "#",
  "hasHeader": true,
  "headerRowCount": 27,
  "skipInitialSpace": true,
  "isDelimited": false,
  "isFixedWidth": true
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix ns1: <dcterms:> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:xasXDIdownload_23463h a cdi:TabularTextDataset,
        schema1:DataDownload ;
    ns1:conformsTo "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md" ;
    cdi:allowsDuplicates false ;
    cdi:has_TextMapping [ a cdi:TextMapping ;
            cdi:formats xas:incidentIntensityVariable ;
            cdi:hasRole "Measure" ;
            cdi:label "i0" ],
        [ a cdi:TextMapping ;
            cdi:formats xas:transmittedIntensityVariable ;
            cdi:hasRole "Measure" ;
            cdi:index 2 ;
            cdi:label "it" ;
            cdi:length 12 ],
        [ a cdi:TextMapping ;
            cdi:formats xas:monochromatorEnergyVariable ;
            cdi:hasRole "Dimension" ;
            cdi:index 1 ;
            cdi:label "energy" ;
            cdi:length 12 ] ;
    schema1:contentSize "30 kb" ;
    schema1:contentUrl "https://github.com/XraySpectroscopy/XASDataLibrary/blob/master/data/Se/Se_Na2SeO4_rt_01.xdi" ;
    schema1:description "Distribution = PhysicalDataSet text file conformant with XDI specification" ;
    schema1:encodingFormat "text/plain" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: definitions for roles used in XAS profile
type: object
properties:
  '@type':
    const: cdi:WideDataStructure
  cdi:has_DataStructureComponent:
    type: array
    items:
      type: object
      properties:
        '@type':
          oneOf:
          - const: cdi:IdentifierComponent
          - const: cdi:MeasureComponent
        cdi:isDefinedBy_InstanceVariable:
          type: object
          description: this must be a reference to a variable defined in the schema:variableMeasured
            part of the metadata record; This condition will need to be validated
            by SHACL rule
          properties:
            '@id':
              type: string
        cdi:has:
          type: object
          properties:
            '@type':
              const: cdi:ValueMapping
            cdi:hasIndex:
              type: integer
            cdi:haslength:
              type: integer
          required:
          - cdi:ValueMapping
      required:
      - cdi:isDefinedBy_InstanceVariable
      - di:has
  cdi:allowsDuplicates:
    type: boolean
    default: false
  cdi:arrayBase:
    type: integer
    default: 1
  cdi:commentPrefix:
    type: string
  cdi:hasHeader:
    type: boolean
  cdi:headerRowCount:
    type: integer
  cdi:skipInitialSpace:
    type: boolean
    default: true
  cdi:isDelimited:
    type: boolean
    default: false
  cdi:isFixedWidth:
    type: boolean
    default: true
required:
- '@type'
- cdi:has_DataStructureComponent
- cdi:hasHeader
- cdi:headerRowCount
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "https://schema.org",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasXdiTabularTextDataset/context.jsonld)

## Sources

* [XDI Format specification](https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/xasProperties/xasXdiTabularTextDataset`

