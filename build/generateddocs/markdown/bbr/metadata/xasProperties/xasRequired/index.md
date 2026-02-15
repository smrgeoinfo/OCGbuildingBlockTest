
# Required Fields for XAS data (Schema)

`cdif.bbr.metadata.xasProperties.xasRequired` *v0.1*

XAS profile files that extend requirements of CDIF discovery. Field content: x-ray source,definition, Data/mode, element/symbol, edge,Instrument/source/type, Instrument/source/name, Instrument/source/probe, Instrument/monochromator/type, Instrument/monochromator/d_spacing, Instrument/monochromator/reflection, Sample/name

[*Status*](http://www.opengis.net/def/status): Under development

## Description

##  XAS profile extension properties

XAS profile files that extend requirements of CDIF discovery. Field content: x-ray source,definition, Data/mode, element/symbol, edge,Instrument/source/type, Instrument/source/name, Instrument/source/probe, Instrument/monochromator/type, Instrument/monochromator/d_spacing, Instrument/monochromator/reflection, Sample/name
## Examples

### Example XAS metadata conforms to required items for extension.
bring together all required properties.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dcterms": "http://purl.org/dc/terms/",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "spdx": "http://spdx.org/rdf/terms#",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "xas": "https://xas.org/dictionary/",
        "nxs": "http://purl.org/nexusformat/definitions/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "prov": "http://www.w3.org/ns/prov#"
    },
    "@id": "NVohEbchV",
    "@type": ["schema:Dataset", "schema:Product"],
    "schema:name": "tniDmCXDxVRXfzMZpjE",
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "BcWkKNjOEqQKZNG",
        "schema:value": "MgxVV",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
    },
    "schema:dateModified": "hTGGhUVjEPFRl",
    "schema:conditionsOfAccess": ["eiSzBJBNrAKINEAkjBAz"],
    "schema:license": ["lWbw", "ZoTXfsfevzu", "ogAgtO", "wVK"],
    "schema:url": "http://example.com/resource?foo=bar#fragment",
    "schema:distribution": [
        {
            "@id": "lMtIx",
            "@type": ["schema:DataDownload", "cdi:PhysicalDataset"],
            "schema:name": "XharpxX",
            "schema:contentUrl": "http://example.com/resource/35uj46j",
            "schema:encodingFormat": ["QmTID"],
            "dcterms:conformsTo": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md",
            "spdx:checksum": {
                "spdx:algorithm": "nLnPEstvn",
                "spdx:checksumValue": "F"
            },
            "schema:provider": [
                {"@id": "plTqxpHjBTESztfaDyI"}
            ]
        },
        {
            "@id": "RNdlTIf",
            "@type": ["schema:DataDownload"],
            "schema:name": "LbbtxfqozvkLlsOZFsXC",
            "schema:contentUrl": "http://example.com/resource/34h5ykl",
            "schema:encodingFormat": ["VMhnXhYenfn", "aVcNGczw"],
            "spdx:checksum": {
                "spdx:algorithm": "CvUDClEiiWFCzNWNoM",
                "spdx:checksumValue": "pObdEeJAdzYLwA"
            },
            "schema:provider": [
                {"@id": "EwHwOWWPjkVxr"}
            ]
        }
    ],
    "schema:subjectOf": {
        "@type": "schema:Dataset",
        "@id": "RUUvGtoRqzVlQELZ",
        "schema:about": {"@id": "NVohEbchV"},
        "dcterms:conformsTo": [
            {"@id": "https://www.opengis.net/def/profile/cdif/discovery"},
            {"@id": "cdif:profile_xasCDIF"}
        ],
        "schema:maintainer": {
            "@id": "nKwywfsuBh",
            "@type": "schema:Person",
            "schema:name": "GyadRNhaueALkWVhXdP"
        },
        "schema:sdDatePublished": "2025-08-15T06:45:40Z",
        "schema:includedInDataCatalog": {
            "@id": "nbUunSyw",
            "@type": "schema:DataCatalog",
            "schema:name": "hFcgszRnAnrDNlkluJ",
            "schema:url": "http://example.com/resource?foo=bar#fragment"
        }
    },
    "prov:wasGeneratedBy": [{
        "prov:used": [
            {
                "@type": ["schema:Thing", "schema:Product"],
                "schema:additionalType": "nxs:BaseClass/NXsource",
                "schema:name": "kVLmQxSource",
                "schema:additionalProperty": [
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["nxs:Field/NXsource/type"],
                        "schema:name": "x-ray source",
                        "schema:value": "Synchrotron X-ray Source"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["nxs:Field/NXsource/probe"],
                        "schema:name": "Probe",
                        "schema:value": "x-ray"
                    }
                ]
            },
            {
                "@type": ["schema:Thing", "schema:Product"],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 111",
                "schema:additionalProperty": [
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["nxs:Field/NXcrystal/d_spacing"],
                        "schema:name": "d-spacing",
                        "schema:value": "3.13550",
                        "schema:unitText": "Angstrom"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["nxs:Field/NXcrystal/type"],
                        "schema:name": "crystal type",
                        "schema:value": "mRqWz"
                    },
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["nxs:Field/NXcrystal/reflection"],
                        "schema:name": "reflection plane (hkl)",
                        "schema:value": "1,1,1"
                    }
                ]
            }
        ],
        "schema:mainEntity": {
            "@type": ["schema:Product", "schema:Thing"],
            "schema:additionalType": [
                "MaterialSample",
                "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
            ],
            "schema:name": "tJSgGfhzZ",
            "schema:identifier": "gGDA",
            "schema:description": "ahjWwyayQYhnB",
            "schema:additionalProperty": [
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["crl"],
                    "schema:name": "nNp",
                    "schema:value": "uUUTOmBQ"
                },
                {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": ["EiAnJhZyLsQAxKd"],
                    "schema:name": "qqcHFymGZzaJLKGN",
                    "schema:value": "rljVqQklQEuNZF"
                }
            ]
        }
    }],
    "schema:measurementTechnique": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "X-Ray Absorption Spectroscopy",
            "schema:termCode": "XAS",
            "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
            "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Transmission",
            "schema:identifier": "bRqVxNm",
            "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
        }
    ],
    "schema:keywords": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "K-edge",
            "schema:identifier": "hYtRv",
            "schema:termCode": "K",
            "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Selenium",
            "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
            "schema:termCode": "Se",
            "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasRequired/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "NVohEbchV",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "tniDmCXDxVRXfzMZpjE",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "BcWkKNjOEqQKZNG",
    "schema:value": "MgxVV",
    "schema:url": "http://example.com/resource?foo=bar#fragment"
  },
  "schema:dateModified": "hTGGhUVjEPFRl",
  "schema:conditionsOfAccess": [
    "eiSzBJBNrAKINEAkjBAz"
  ],
  "schema:license": [
    "lWbw",
    "ZoTXfsfevzu",
    "ogAgtO",
    "wVK"
  ],
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:distribution": [
    {
      "@id": "lMtIx",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataset"
      ],
      "schema:name": "XharpxX",
      "schema:contentUrl": "http://example.com/resource/35uj46j",
      "schema:encodingFormat": [
        "QmTID"
      ],
      "dcterms:conformsTo": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md",
      "spdx:checksum": {
        "spdx:algorithm": "nLnPEstvn",
        "spdx:checksumValue": "F"
      },
      "schema:provider": [
        {
          "@id": "plTqxpHjBTESztfaDyI"
        }
      ]
    },
    {
      "@id": "RNdlTIf",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "LbbtxfqozvkLlsOZFsXC",
      "schema:contentUrl": "http://example.com/resource/34h5ykl",
      "schema:encodingFormat": [
        "VMhnXhYenfn",
        "aVcNGczw"
      ],
      "spdx:checksum": {
        "spdx:algorithm": "CvUDClEiiWFCzNWNoM",
        "spdx:checksumValue": "pObdEeJAdzYLwA"
      },
      "schema:provider": [
        {
          "@id": "EwHwOWWPjkVxr"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": "schema:Dataset",
    "@id": "RUUvGtoRqzVlQELZ",
    "schema:about": {
      "@id": "NVohEbchV"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://www.opengis.net/def/profile/cdif/discovery"
      },
      {
        "@id": "cdif:profile_xasCDIF"
      }
    ],
    "schema:maintainer": {
      "@id": "nKwywfsuBh",
      "@type": "schema:Person",
      "schema:name": "GyadRNhaueALkWVhXdP"
    },
    "schema:sdDatePublished": "2025-08-15T06:45:40Z",
    "schema:includedInDataCatalog": {
      "@id": "nbUunSyw",
      "@type": "schema:DataCatalog",
      "schema:name": "hFcgszRnAnrDNlkluJ",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": "nxs:BaseClass/NXsource",
          "schema:name": "kVLmQxSource",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXsource/type"
              ],
              "schema:name": "x-ray source",
              "schema:value": "Synchrotron X-ray Source"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXsource/probe"
              ],
              "schema:name": "Probe",
              "schema:value": "x-ray"
            }
          ]
        },
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": "nxs:BaseClass/NXmonochromator",
          "schema:name": "Si 111",
          "schema:additionalProperty": [
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/d_spacing"
              ],
              "schema:name": "d-spacing",
              "schema:value": "3.13550",
              "schema:unitText": "Angstrom"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/type"
              ],
              "schema:name": "crystal type",
              "schema:value": "mRqWz"
            },
            {
              "@type": "schema:PropertyValue",
              "schema:propertyID": [
                "nxs:Field/NXcrystal/reflection"
              ],
              "schema:name": "reflection plane (hkl)",
              "schema:value": "1,1,1"
            }
          ]
        }
      ],
      "schema:mainEntity": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "tJSgGfhzZ",
        "schema:identifier": "gGDA",
        "schema:description": "ahjWwyayQYhnB",
        "schema:additionalProperty": [
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "crl"
            ],
            "schema:name": "nNp",
            "schema:value": "uUUTOmBQ"
          },
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "EiAnJhZyLsQAxKd"
            ],
            "schema:name": "qqcHFymGZzaJLKGN",
            "schema:value": "rljVqQklQEuNZF"
          }
        ]
      }
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Transmission",
      "schema:identifier": "bRqVxNm",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "K-edge",
      "schema:identifier": "hYtRv",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

<file:///github/workspace/NVohEbchV> a schema1:Dataset,
        schema1:Product ;
    schema1:conditionsOfAccess "eiSzBJBNrAKINEAkjBAz" ;
    schema1:dateModified "hTGGhUVjEPFRl" ;
    schema1:distribution <file:///github/workspace/RNdlTIf>,
        <file:///github/workspace/lMtIx> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "BcWkKNjOEqQKZNG" ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "MgxVV" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "hYtRv" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ] ;
    schema1:license "ZoTXfsfevzu",
        "lWbw",
        "ogAgtO",
        "wVK" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "bRqVxNm" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ] ;
    schema1:name "tniDmCXDxVRXfzMZpjE" ;
    schema1:subjectOf <file:///github/workspace/RUUvGtoRqzVlQELZ> ;
    schema1:url "http://example.com/resource?foo=bar#fragment" ;
    prov:wasGeneratedBy [ schema1:mainEntity [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "nNp" ;
                            schema1:propertyID "crl" ;
                            schema1:value "uUUTOmBQ" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "qqcHFymGZzaJLKGN" ;
                            schema1:propertyID "EiAnJhZyLsQAxKd" ;
                            schema1:value "rljVqQklQEuNZF" ] ;
                    schema1:additionalType "MaterialSample",
                        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
                    schema1:description "ahjWwyayQYhnB" ;
                    schema1:identifier "gGDA" ;
                    schema1:name "tJSgGfhzZ" ] ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "reflection plane (hkl)" ;
                            schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                            schema1:value "1,1,1" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "d-spacing" ;
                            schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                            schema1:unitText "Angstrom" ;
                            schema1:value "3.13550" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "crystal type" ;
                            schema1:propertyID "nxs:Field/NXcrystal/type" ;
                            schema1:value "mRqWz" ] ;
                    schema1:additionalType "nxs:BaseClass/NXmonochromator" ;
                    schema1:name "Si 111" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Probe" ;
                            schema1:propertyID "nxs:Field/NXsource/probe" ;
                            schema1:value "x-ray" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "x-ray source" ;
                            schema1:propertyID "nxs:Field/NXsource/type" ;
                            schema1:value "Synchrotron X-ray Source" ] ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "kVLmQxSource" ] ] .

<file:///github/workspace/RNdlTIf> a schema1:DataDownload ;
    schema1:contentUrl "http://example.com/resource/34h5ykl" ;
    schema1:encodingFormat "VMhnXhYenfn",
        "aVcNGczw" ;
    schema1:name "LbbtxfqozvkLlsOZFsXC" ;
    schema1:provider <file:///github/workspace/EwHwOWWPjkVxr> ;
    spdx:checksum [ spdx:algorithm "CvUDClEiiWFCzNWNoM" ;
            spdx:checksumValue "pObdEeJAdzYLwA" ] .

<file:///github/workspace/RUUvGtoRqzVlQELZ> a schema1:Dataset ;
    dcterms:conformsTo <cdif:profile_xasCDIF>,
        <https://www.opengis.net/def/profile/cdif/discovery> ;
    schema1:about <file:///github/workspace/NVohEbchV> ;
    schema1:includedInDataCatalog <file:///github/workspace/nbUunSyw> ;
    schema1:maintainer <file:///github/workspace/nKwywfsuBh> ;
    schema1:sdDatePublished "2025-08-15T06:45:40Z" .

<file:///github/workspace/lMtIx> a cdi:PhysicalDataset,
        schema1:DataDownload ;
    dcterms:conformsTo "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md" ;
    schema1:contentUrl "http://example.com/resource/35uj46j" ;
    schema1:encodingFormat "QmTID" ;
    schema1:name "XharpxX" ;
    schema1:provider <file:///github/workspace/plTqxpHjBTESztfaDyI> ;
    spdx:checksum [ spdx:algorithm "nLnPEstvn" ;
            spdx:checksumValue "F" ] .

<file:///github/workspace/nKwywfsuBh> a schema1:Person ;
    schema1:name "GyadRNhaueALkWVhXdP" .

<file:///github/workspace/nbUunSyw> a schema1:DataCatalog ;
    schema1:name "hFcgszRnAnrDNlkluJ" ;
    schema1:url "http://example.com/resource?foo=bar#fragment" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: '#/$defs/CdifMandatory'
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
        enum:
        - schema:Dataset
        - schema:Product
    schema:subjectOf:
      $ref: '#/$defs/XasSubject'
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            description: 'array of instrument or instrument system components. The
              x-ray source type and probe,  and monochromator properties type, d-spacing
              and reflection plane are required '
            items:
              type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                schema:additionalType:
                  type: string
                schema:additionalProperty:
                  type: array
                  items:
                    $ref: '#/$defs/AdditionalProperty'
            minItems: 2
            allOf:
            - contains:
                type: object
                properties:
                  '@type':
                    type: array
                    items:
                      type: string
                    minItems: 2
                    allOf:
                    - contains:
                        const: schema:Thing
                    - contains:
                        const: schema:Product
                  schema:additionalType:
                    const: nxs:BaseClass/NXsource
                  schema:additionalProperty:
                    type: array
                    minItems: 2
                    items:
                      $ref: '#/$defs/AdditionalProperty'
                    allOf:
                    - contains:
                        type: object
                        properties:
                          schema:propertyID:
                            type: array
                            contains:
                              const: nxs:Field/NXsource/type
                          schema:value:
                            type: string
                        required:
                        - schema:propertyID
                        - schema:value
                    - contains:
                        type: object
                        properties:
                          schema:propertyID:
                            type: array
                            contains:
                              const: nxs:Field/NXsource/probe
                          schema:name:
                            const: Probe
                          schema:value:
                            type: string
                        required:
                        - schema:name
                        - schema:propertyID
                        - schema:value
                required:
                - '@type'
                - schema:additionalType
                - schema:additionalProperty
            - contains:
                type: object
                properties:
                  '@type':
                    type: array
                    items:
                      type: string
                    minItems: 2
                    allOf:
                    - contains:
                        const: schema:Thing
                    - contains:
                        const: schema:Product
                  schema:additionalType:
                    const: nxs:BaseClass/NXmonochromator
                  schema:name:
                    type: string
                  schema:additionalProperty:
                    description: Require additional properties for monochromator,
                      requires d-space, crystal type, reflection plane.
                    type: array
                    minItems: 3
                    items:
                      $ref: '#/$defs/AdditionalProperty'
                    contains:
                      type: object
                      properties:
                        schema:propertyID:
                          type: array
                          contains:
                            const: nxs:Field/NXcrystal/type
                        schema:value:
                          type: string
                      required:
                      - schema:value
                      - schema:propertyID
                    allOf:
                    - contains:
                        type: object
                        properties:
                          schema:propertyID:
                            type: array
                            contains:
                              const: nxs:Field/NXcrystal/d_spacing
                          schema:value:
                            type: string
                          schema:unitText:
                            type: string
                        required:
                        - schema:propertyID
                        - schema:value
                        - schema:unitText
                    - contains:
                        type: object
                        properties:
                          schema:propertyID:
                            type: array
                            contains:
                              const: nxs:Field/NXcrystal/reflection
                          schema:value:
                            type: string
                        required:
                        - schema:value
                        - schema:propertyID
                required:
                - '@type'
                - schema:additionalType
                - schema:additionalProperty
          schema:mainEntity:
            $ref: '#/$defs/XasSample'
    schema:distribution:
      type: array
      items:
        $ref: '#/$defs/DataDownload'
      contains:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 2
            allOf:
            - contains:
                const: schema:DataDownload
            - contains:
                const: cdi:PhysicalDataset
          dcterms:conformsTo:
            const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md
        required:
        - '@type'
        - dcterms:conformsTo
    schema:measurementTechnique:
      type: array
      description: 'Require DefinedTerms for both: absorption edge (XDI dict) and
        target element (SWEET).'
      minItems: 2
      items:
        $ref: '#/$defs/DefinedTerm'
      contains:
        type: object
        properties:
          schema:name:
            const: X-Ray Absorption Spectroscopy
          schema:termCode:
            const: XAS
          schema:identifier:
            const: http://purl.org/pan-science/PaNET/PaNET01196
          schema:inDefinedTermSet:
            const: http://purl.org/pan-science/PaNET/PaNET.owl
        required:
        - schema:name
        - schema:termCode
        - schema:identifier
        - schema:inDefinedTermSet
      allOf:
      - contains:
          type: object
          properties:
            schema:name:
              type: string
            schema:inDefinedTermSet:
              const: nxs:Field/NXxas/ENTRY/DATA/mode
          required:
          - schema:name
          - schema:inDefinedTermSet
    schema:keywords:
      type: array
      description: extends base CDIF keyword schema to require defined terms for the
        absorption edge and the target element for the analysis
      minItems: 2
      items:
        type: object
        properties:
          '@type':
            const: schema:DefinedTerm
          schema:name:
            type: string
          schema:identifier:
            type: string
          schema:inDefinedTermSet:
            type: string
            description: need to include this to tag what the keyword is about; we're
              using the keywords as soft-typed properties
        required:
        - '@type'
        - schema:name
        - schema:inDefinedTermSet
        additionalProperties: true
      contains:
        type: object
        properties:
          schema:inDefinedTermSet:
            const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
        required:
        - schema:inDefinedTermSet
      allOf:
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: http://sweetontology.net/matrElement
          required:
          - schema:inDefinedTermSet
$defs:
  CdifMandatory:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/cdifMandatory/cdifMandatorySchema.json
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/definedTermSchema.json
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/additionalProperty/additionalPropertySchema.json
  DataDownload:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/dataDownload/dataDownloadSchema.json
  XasSample:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/xasProperties/xasSample/xasSampleSchema.json
  XasSubject:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/xasProperties/xasSubject/xasSubjectSchema.json
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasRequired/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasRequired/schema.yaml)


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
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasRequired/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasRequired`

