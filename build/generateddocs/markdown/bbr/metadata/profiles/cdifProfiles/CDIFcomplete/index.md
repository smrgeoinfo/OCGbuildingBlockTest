
# CDIF complete metadata (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFcomplete` *v0.1*

Profile combining CDIF discovery metadata with data description extensions for distributions (single-file, archive with hasPart, and WebAPI) and optional tabular/dataCube physical mappings

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF complete metadata properties

Profile assembling building blocks for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) complete profile. Extends the CDIFDiscovery profile with data description and archive distribution extensions.

### Composition

- **CDIFDiscovery** — mandatory and optional discovery metadata (cdifMandatory + cdifOptional), including variableMeasured descriptions
- **Data description extensions** — distribution items may include CDIF data description properties:
  - `cdifTabularData` — for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
  - `cdifDataCube` — for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings
- **Archive distribution** (`cdifArchiveDistribution`) — for archive files (ZIP, tar.gz) containing multiple component files described via `schema:hasPart`, each typed as `schema:MediaObject` with optional data description extensions
- **WebAPI distribution** — for API-based data access with `schema:potentialAction` describing query endpoints and result data descriptions

### Distribution types

Each `schema:distribution` item must match one of:

1. **Single-file DataDownload** — a directly accessible file with optional tabular/dataCube data description
2. **Archive DataDownload** — an archive file with `schema:hasPart` listing component files
3. **WebAPI** — an API endpoint with `schema:potentialAction` describing available queries and their result format

## Examples

### CDIF complete profile example record.
Comprehensive CDIF metadata example demonstrating the complete profile with
discovery metadata, single-file and archive distributions with component files,
WebAPI access, tabular and data cube physical mappings, provenance, and
quality measurements.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dcterms": "http://purl.org/dc/terms/",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "spdx": "http://spdx.org/rdf/terms#",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "csvw": "http://www.w3.org/ns/csvw#",
        "prov": "http://www.w3.org/ns/prov#",
        "ex": "https://example.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "ex:complete-dataset-001",
    "@type": ["schema:Dataset"],
    "schema:name": "Multi-technique geochemistry dataset with archive and API access",
    "schema:description": "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint.",
    "schema:additionalType": ["geochemistry analysis"],
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://registry.identifiers.org/registry/doi",
        "schema:value": "10.5880/example.complete.001",
        "schema:url": "https://doi.org/10.5880/example.complete.001"
    },
    "schema:sameAs": [
        {
            "@type": "schema:PropertyValue",
            "schema:value": "urn:example:geochem:complete-001"
        }
    ],
    "schema:version": "1.0",
    "schema:url": "https://example.org/datasets/complete-001",
    "schema:inLanguage": "en",
    "schema:dateModified": "2026-02-15",
    "schema:datePublished": "2026-02-01",
    "schema:license": ["https://creativecommons.org/licenses/by/4.0/"],
    "schema:conditionsOfAccess": ["Open access; citation required"],
    "schema:keywords": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "geochemistry",
            "schema:identifier": {
                "@type": "schema:PropertyValue",
                "schema:propertyID": "https://vocabularyserver.com/keyword",
                "schema:value": "geochem-001",
                "schema:url": "https://vocabularyserver.com/keyword/geochem-001"
            },
            "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
            "schema:termCode": "GEOCHEM"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "spectral analysis",
            "schema:identifier": {
                "@type": "schema:PropertyValue",
                "schema:propertyID": "https://vocabularyserver.com/keyword",
                "schema:value": "spectral-001",
                "schema:url": "https://vocabularyserver.com/keyword/spectral-001"
            },
            "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
            "schema:termCode": "SPECTRAL"
        }
    ],
    "schema:creator": {
        "@list": [
            {
                "@id": "https://orcid.org/0000-0001-2345-6789",
                "@type": "schema:Person",
                "schema:name": "Smith, Jane",
                "schema:alternateName": "J. Smith",
                "schema:affiliation": {
                    "@id": "https://ror.org/03m2x1q45",
                    "@type": "schema:Organization",
                    "schema:name": "University of Arizona"
                },
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "jsmith@arizona.edu"
                },
                "schema:identifier": {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "https://orcid.org",
                    "schema:value": "0000-0001-2345-6789",
                    "schema:url": "https://orcid.org/0000-0001-2345-6789"
                }
            }
        ]
    },
    "schema:publisher": {
        "@id": "ex:ieda-publisher",
        "@type": "schema:Organization",
        "schema:name": "IEDA",
        "schema:alternateName": "Interdisciplinary Earth Data Alliance",
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://registry.identifiers.org/registry/ror",
            "schema:value": "02fjgr047",
            "schema:url": "https://ror.org/02fjgr047"
        }
    },
    "schema:funding": [
        {
            "@type": "schema:MonetaryGrant",
            "schema:identifier": {
                "@type": "schema:PropertyValue",
                "schema:propertyID": "NSF award number",
                "schema:value": "EAR-2026932",
                "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932"
            },
            "schema:name": "Geochemistry Data Infrastructure",
            "schema:funder": {"@id": "https://ror.org/021nxhr62"}
        }
    ],
    "schema:distribution": [
        {
            "@type": ["schema:DataDownload"],
            "schema:name": "Geochemistry summary results",
            "schema:contentUrl": "https://example.org/data/geochem-summary.csv",
            "schema:encodingFormat": ["text/csv"],
            "spdx:checksum": {
                "spdx:algorithm": "SHA256",
                "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
            }
        },
        {
            "@type": ["schema:DataDownload", "cdi:TabularTextDataSet"],
            "schema:name": "Detailed geochemistry analysis results",
            "schema:contentUrl": "https://example.org/data/geochem-detailed.csv",
            "schema:encodingFormat": ["text/csv"],
            "spdx:checksum": {
                "spdx:algorithm": "SHA256",
                "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
            },
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "countRows": 461,
            "countColumns": 3,
            "cdi:hasPhysicalMapping": [
                {
                    "cdi:index": 0,
                    "cdi:format": "string",
                    "cdi:physicalDataType": "string",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {"@id": "ex:var-sampleID"}
                },
                {
                    "cdi:index": 1,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float64",
                    "cdi:nullSequence": "NA",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {"@id": "ex:var-concentration"}
                },
                {
                    "cdi:index": 2,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float64",
                    "cdi:nullSequence": "-9999",
                    "cdi:isRequired": false,
                    "cdi:formats_InstanceVariable": {"@id": "ex:var-uncertainty"}
                }
            ]
        },
        {
            "@type": ["schema:DataDownload", "cdi:StructuredDataSet"],
            "schema:name": "Spectral data cube",
            "schema:contentUrl": "https://example.org/data/spectra-cube.nc",
            "schema:encodingFormat": ["application/x-netcdf"],
            "spdx:checksum": {
                "spdx:algorithm": "SHA256",
                "spdx:checksumValue": "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
            },
            "cdi:hasPhysicalMapping": [
                {
                    "cdi:index": 0,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float32",
                    "cdi:locator": "/spectra/wavelength",
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {"@id": "ex:var-wavelength"}
                },
                {
                    "cdi:index": 1,
                    "cdi:format": "decimal",
                    "cdi:physicalDataType": "float32",
                    "cdi:locator": "/spectra/intensity",
                    "cdi:scale": 1000,
                    "cdi:isRequired": true,
                    "cdi:formats_InstanceVariable": {"@id": "ex:var-intensity"}
                }
            ]
        },
        {
            "@type": ["schema:DataDownload"],
            "schema:name": "Complete data package",
            "schema:contentUrl": "https://example.org/data/geochem-package.zip",
            "schema:encodingFormat": ["application/zip"],
            "schema:description": "Archive containing all data files. Component files are listed as parts and are not individually accessible.",
            "spdx:checksum": {
                "spdx:algorithm": "SHA256",
                "spdx:checksumValue": "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
            },
            "schema:hasPart": [
                {
                    "@type": ["schema:MediaObject"],
                    "@id": "#part-results-csv",
                    "schema:name": "geochem-detailed.csv",
                    "schema:description": "Detailed geochemistry analysis results in tabular format.",
                    "schema:encodingFormat": ["text/csv"],
                    "schema:size": {
                        "@type": "schema:QuantitativeValue",
                        "schema:value": 10860,
                        "schema:unitText": "byte"
                    },
                    "spdx:checksum": {
                        "spdx:algorithm": "SHA256",
                        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
                    }
                },
                {
                    "@type": ["schema:MediaObject", "cdi:TabularTextDataSet"],
                    "@id": "#part-measurements-csv",
                    "schema:name": "geochem-measurements.csv",
                    "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
                    "schema:encodingFormat": ["text/csv"],
                    "schema:size": {
                        "@type": "schema:QuantitativeValue",
                        "schema:value": 6249,
                        "schema:unitText": "byte"
                    },
                    "cdi:isDelimited": true,
                    "csvw:delimiter": ",",
                    "csvw:header": true,
                    "csvw:headerRowCount": 1,
                    "countRows": 144,
                    "countColumns": 3,
                    "cdi:hasPhysicalMapping": [
                        {
                            "cdi:index": 0,
                            "cdi:format": "string",
                            "cdi:physicalDataType": "string",
                            "cdi:isRequired": true
                        },
                        {
                            "cdi:index": 1,
                            "cdi:format": "decimal",
                            "cdi:physicalDataType": "float64",
                            "cdi:nullSequence": "NA",
                            "cdi:isRequired": true
                        },
                        {
                            "cdi:index": 2,
                            "cdi:format": "decimal",
                            "cdi:physicalDataType": "float64",
                            "cdi:nullSequence": "NA",
                            "cdi:isRequired": false
                        }
                    ]
                },
                {
                    "@type": ["schema:MediaObject", "cdi:StructuredDataSet"],
                    "@id": "#part-spectra-nc",
                    "schema:name": "spectra-cube.nc",
                    "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
                    "schema:encodingFormat": ["application/x-netcdf"],
                    "schema:size": {
                        "@type": "schema:QuantitativeValue",
                        "schema:value": 13743003,
                        "schema:unitText": "byte"
                    },
                    "cdi:hasPhysicalMapping": [
                        {
                            "cdi:index": 0,
                            "cdi:format": "decimal",
                            "cdi:physicalDataType": "float32",
                            "cdi:locator": "/spectra/wavelength",
                            "cdi:isRequired": true
                        },
                        {
                            "cdi:index": 1,
                            "cdi:format": "decimal",
                            "cdi:physicalDataType": "float32",
                            "cdi:locator": "/spectra/intensity",
                            "cdi:isRequired": true
                        }
                    ]
                },
                {
                    "@type": ["schema:MediaObject"],
                    "@id": "#part-method-pdf",
                    "schema:name": "analysis-method.pdf",
                    "schema:description": "Method description document for the analysis.",
                    "schema:encodingFormat": ["application/pdf"],
                    "schema:size": {
                        "@type": "schema:QuantitativeValue",
                        "schema:value": 56062,
                        "schema:unitText": "byte"
                    }
                },
                {
                    "@type": ["schema:MediaObject"],
                    "@id": "#part-metadata-yaml",
                    "schema:name": "geochem-detailed-metadata.yaml",
                    "schema:description": "Metadata sidecar for the results CSV file.",
                    "schema:encodingFormat": ["application/yaml"],
                    "schema:size": {
                        "@type": "schema:QuantitativeValue",
                        "schema:value": 2281,
                        "schema:unitText": "byte"
                    },
                    "schema:about": [{"@id": "#part-results-csv"}]
                }
            ]
        },
        {
            "@type": ["schema:WebAPI"],
            "schema:serviceType": {
                "@type": "schema:DefinedTerm",
                "schema:name": "OGC API - Features",
                "schema:identifier": {
                    "@type": "schema:PropertyValue",
                    "schema:propertyID": "https://www.ogc.org/standards",
                    "schema:value": "ogcapi-features-1",
                    "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
                },
                "schema:inDefinedTermSet": "https://www.ogc.org/standards",
                "schema:termCode": "ogcapi-features"
            },
            "schema:termsOfService": "Open access, no authentication required",
            "schema:documentation": {
                "@type": "schema:CreativeWork",
                "schema:name": "OpenAPI specification for geochemistry data service",
                "schema:url": "https://example.org/api/v1/openapi.json"
            },
            "schema:potentialAction": [
                {
                    "@type": "schema:Action",
                    "schema:name": "Query geochemistry features",
                    "schema:target": {
                        "@type": "schema:EntryPoint",
                        "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
                        "schema:urlTemplate": "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
                        "schema:httpMethod": ["GET"],
                        "schema:contentType": ["text/csv", "application/geo+json"]
                    },
                    "schema:result": {
                        "@type": ["schema:DataDownload"],
                        "schema:name": "Geochemistry query results",
                        "schema:contentUrl": "https://example.org/api/v1/collections/geochem/items?f=csv",
                        "schema:encodingFormat": ["text/csv"],
                        "cdi:isDelimited": true,
                        "csvw:delimiter": ",",
                        "csvw:header": true,
                        "csvw:headerRowCount": 1,
                        "cdi:hasPhysicalMapping": [
                            {
                                "cdi:index": 0,
                                "cdi:format": "decimal",
                                "cdi:physicalDataType": "float64",
                                "cdi:isRequired": true,
                                "cdi:formats_InstanceVariable": {"@id": "ex:var-concentration"}
                            },
                            {
                                "cdi:index": 1,
                                "cdi:format": "decimal",
                                "cdi:physicalDataType": "float64",
                                "cdi:isRequired": false,
                                "cdi:formats_InstanceVariable": {"@id": "ex:var-uncertainty"}
                            }
                        ]
                    },
                    "schema:object": {
                        "@type": "schema:DataFeed",
                        "schema:description": "Geochemistry observations collection"
                    },
                    "schema:query-input": [
                        {
                            "@type": "schema:PropertyValueSpecification",
                            "schema:valueName": "format",
                            "schema:description": "Response format: csv or geojson",
                            "schema:valueRequired": false,
                            "schema:valuePattern": "csv|geojson"
                        },
                        {
                            "@type": "schema:PropertyValueSpecification",
                            "schema:valueName": "limit",
                            "schema:description": "Maximum number of features to return",
                            "schema:valueRequired": false
                        },
                        {
                            "@type": "schema:PropertyValueSpecification",
                            "schema:valueName": "offset",
                            "schema:description": "Starting index for pagination",
                            "schema:valueRequired": false
                        }
                    ]
                }
            ]
        }
    ],
    "schema:variableMeasured": [
        {
            "@type": ["schema:PropertyValue"],
            "@id": "ex:var-sampleID",
            "schema:name": "Sample identifier",
            "schema:description": "Unique identifier for each sample",
            "schema:propertyID": ["urn:example:property:sampleID"]
        },
        {
            "@type": ["schema:PropertyValue"],
            "@id": "ex:var-concentration",
            "schema:name": "Element concentration",
            "schema:description": "Measured element concentration in parts per million",
            "schema:propertyID": ["urn:example:property:concentration"],
            "schema:measurementTechnique": "ICP-MS",
            "schema:unitText": "ppm",
            "schema:unitCode": "59",
            "schema:minValue": 0.01,
            "schema:maxValue": 5000
        },
        {
            "@type": ["schema:PropertyValue"],
            "@id": "ex:var-uncertainty",
            "schema:name": "Measurement uncertainty",
            "schema:description": "2-sigma uncertainty on concentration measurement",
            "schema:propertyID": ["urn:example:property:uncertainty"],
            "schema:unitText": "ppm",
            "schema:unitCode": "59"
        },
        {
            "@type": ["schema:PropertyValue"],
            "@id": "ex:var-wavelength",
            "schema:name": "Wavelength",
            "schema:description": "Spectral wavelength",
            "schema:propertyID": ["urn:example:property:wavelength"],
            "schema:unitText": "nm",
            "schema:minValue": 200,
            "schema:maxValue": 2500
        },
        {
            "@type": ["schema:PropertyValue"],
            "@id": "ex:var-intensity",
            "schema:name": "Spectral intensity",
            "schema:description": "Measured spectral intensity",
            "schema:propertyID": ["urn:example:property:intensity"],
            "schema:unitText": "counts"
        }
    ],
    "schema:subjectOf": {
        "@type": "schema:Dataset",
        "@id": "ex:metadata-record-001",
        "schema:about": {"@id": "ex:complete-dataset-001"},
        "dcterms:conformsTo": [
            {"@id": "https://example.org/profiles/CDIFcomplete/v0.1"}
        ],
        "schema:maintainer": {
            "@id": "https://orcid.org/0000-0001-2345-6789",
            "@type": "schema:Person",
            "schema:name": "Smith, Jane",
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "jsmith@arizona.edu"
            }
        },
        "schema:sdDatePublished": "2026-02-19",
        "schema:includedInDataCatalog": {
            "@id": "ex:ieda-catalog",
            "@type": "schema:DataCatalog",
            "schema:name": "IEDA Data Catalog",
            "schema:url": "https://www.earthchem.org/"
        }
    }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:complete-dataset-001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Multi-technique geochemistry dataset with archive and API access",
  "schema:description": "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint.",
  "schema:additionalType": [
    "geochemistry analysis"
  ],
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.5880/example.complete.001",
    "schema:url": "https://doi.org/10.5880/example.complete.001"
  },
  "schema:sameAs": [
    {
      "@type": "schema:PropertyValue",
      "schema:value": "urn:example:geochem:complete-001"
    }
  ],
  "schema:version": "1.0",
  "schema:url": "https://example.org/datasets/complete-001",
  "schema:inLanguage": "en",
  "schema:dateModified": "2026-02-15",
  "schema:datePublished": "2026-02-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:conditionsOfAccess": [
    "Open access; citation required"
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "geochemistry",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "geochem-001",
        "schema:url": "https://vocabularyserver.com/keyword/geochem-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "GEOCHEM"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "spectral analysis",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "spectral-001",
        "schema:url": "https://vocabularyserver.com/keyword/spectral-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "SPECTRAL"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-2345-6789",
        "@type": "schema:Person",
        "schema:name": "Smith, Jane",
        "schema:alternateName": "J. Smith",
        "schema:affiliation": {
          "@id": "https://ror.org/03m2x1q45",
          "@type": "schema:Organization",
          "schema:name": "University of Arizona"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "jsmith@arizona.edu"
        },
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-2345-6789",
          "schema:url": "https://orcid.org/0000-0001-2345-6789"
        }
      }
    ]
  },
  "schema:publisher": {
    "@id": "ex:ieda-publisher",
    "@type": "schema:Organization",
    "schema:name": "IEDA",
    "schema:alternateName": "Interdisciplinary Earth Data Alliance",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "02fjgr047",
      "schema:url": "https://ror.org/02fjgr047"
    }
  },
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "NSF award number",
        "schema:value": "EAR-2026932",
        "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932"
      },
      "schema:name": "Geochemistry Data Infrastructure",
      "schema:funder": {
        "@id": "https://ror.org/021nxhr62"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geochemistry summary results",
      "schema:contentUrl": "https://example.org/data/geochem-summary.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      }
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet"
      ],
      "schema:name": "Detailed geochemistry analysis results",
      "schema:contentUrl": "https://example.org/data/geochem-detailed.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "countRows": 461,
      "countColumns": 3,
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "string",
          "cdi:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-sampleID"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-concentration"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-uncertainty"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet"
      ],
      "schema:name": "Spectral data cube",
      "schema:contentUrl": "https://example.org/data/spectra-cube.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
      },
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/wavelength",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-wavelength"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/intensity",
          "cdi:scale": 1000,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-intensity"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Complete data package",
      "schema:contentUrl": "https://example.org/data/geochem-package.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:description": "Archive containing all data files. Component files are listed as parts and are not individually accessible.",
      "spdx:checksum": {
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
      },
      "schema:hasPart": [
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-results-csv",
          "schema:name": "geochem-detailed.csv",
          "schema:description": "Detailed geochemistry analysis results in tabular format.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 10860,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "spdx:algorithm": "SHA256",
            "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
          }
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet"
          ],
          "@id": "#part-measurements-csv",
          "schema:name": "geochem-measurements.csv",
          "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 6249,
            "schema:unitText": "byte"
          },
          "cdi:isDelimited": true,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "csvw:headerRowCount": 1,
          "countRows": 144,
          "countColumns": 3,
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "string",
              "cdi:physicalDataType": "string",
              "cdi:isRequired": true
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": true
            },
            {
              "cdi:index": 2,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": false
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:StructuredDataSet"
          ],
          "@id": "#part-spectra-nc",
          "schema:name": "spectra-cube.nc",
          "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
          "schema:encodingFormat": [
            "application/x-netcdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 13743003,
            "schema:unitText": "byte"
          },
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/wavelength",
              "cdi:isRequired": true
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/intensity",
              "cdi:isRequired": true
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-method-pdf",
          "schema:name": "analysis-method.pdf",
          "schema:description": "Method description document for the analysis.",
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 56062,
            "schema:unitText": "byte"
          }
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-metadata-yaml",
          "schema:name": "geochem-detailed-metadata.yaml",
          "schema:description": "Metadata sidecar for the results CSV file.",
          "schema:encodingFormat": [
            "application/yaml"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 2281,
            "schema:unitText": "byte"
          },
          "schema:about": [
            {
              "@id": "#part-results-csv"
            }
          ]
        }
      ]
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:serviceType": {
        "@type": "schema:DefinedTerm",
        "schema:name": "OGC API - Features",
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://www.ogc.org/standards",
          "schema:value": "ogcapi-features-1",
          "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
        },
        "schema:inDefinedTermSet": "https://www.ogc.org/standards",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required",
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "OpenAPI specification for geochemistry data service",
        "schema:url": "https://example.org/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": "schema:Action",
          "schema:name": "Query geochemistry features",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
            "schema:urlTemplate": "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
            "schema:httpMethod": [
              "GET"
            ],
            "schema:contentType": [
              "text/csv",
              "application/geo+json"
            ]
          },
          "schema:result": {
            "@type": [
              "schema:DataDownload"
            ],
            "schema:name": "Geochemistry query results",
            "schema:contentUrl": "https://example.org/api/v1/collections/geochem/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdi:hasPhysicalMapping": [
              {
                "cdi:index": 0,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": true,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:var-concentration"
                }
              },
              {
                "cdi:index": 1,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:var-uncertainty"
                }
              }
            ]
          },
          "schema:object": {
            "@type": "schema:DataFeed",
            "schema:description": "Geochemistry observations collection"
          },
          "schema:query-input": [
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "format",
              "schema:description": "Response format: csv or geojson",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv|geojson"
            },
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "limit",
              "schema:description": "Maximum number of features to return",
              "schema:valueRequired": false
            },
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "offset",
              "schema:description": "Starting index for pagination",
              "schema:valueRequired": false
            }
          ]
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "@id": "ex:var-sampleID",
      "schema:name": "Sample identifier",
      "schema:description": "Unique identifier for each sample",
      "schema:propertyID": [
        "urn:example:property:sampleID"
      ]
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "@id": "ex:var-concentration",
      "schema:name": "Element concentration",
      "schema:description": "Measured element concentration in parts per million",
      "schema:propertyID": [
        "urn:example:property:concentration"
      ],
      "schema:measurementTechnique": "ICP-MS",
      "schema:unitText": "ppm",
      "schema:unitCode": "59",
      "schema:minValue": 0.01,
      "schema:maxValue": 5000
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "@id": "ex:var-uncertainty",
      "schema:name": "Measurement uncertainty",
      "schema:description": "2-sigma uncertainty on concentration measurement",
      "schema:propertyID": [
        "urn:example:property:uncertainty"
      ],
      "schema:unitText": "ppm",
      "schema:unitCode": "59"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "@id": "ex:var-wavelength",
      "schema:name": "Wavelength",
      "schema:description": "Spectral wavelength",
      "schema:propertyID": [
        "urn:example:property:wavelength"
      ],
      "schema:unitText": "nm",
      "schema:minValue": 200,
      "schema:maxValue": 2500
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "@id": "ex:var-intensity",
      "schema:name": "Spectral intensity",
      "schema:description": "Measured spectral intensity",
      "schema:propertyID": [
        "urn:example:property:intensity"
      ],
      "schema:unitText": "counts"
    }
  ],
  "schema:subjectOf": {
    "@type": "schema:Dataset",
    "@id": "ex:metadata-record-001",
    "schema:about": {
      "@id": "ex:complete-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://example.org/profiles/CDIFcomplete/v0.1"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/0000-0001-2345-6789",
      "@type": "schema:Person",
      "schema:name": "Smith, Jane",
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "jsmith@arizona.edu"
      }
    },
    "schema:sdDatePublished": "2026-02-19",
    "schema:includedInDataCatalog": {
      "@id": "ex:ieda-catalog",
      "@type": "schema:DataCatalog",
      "schema:name": "IEDA Data Catalog",
      "schema:url": "https://www.earthchem.org/"
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#part-measurements-csv> a cdi:TabularTextDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ],
        [ cdi:format "string" ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:physicalDataType "string" ],
        [ cdi:format "decimal" ;
            cdi:index 2 ;
            cdi:isRequired false ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ] ;
    cdi:isDelimited true ;
    schema1:description "Measurement data with column structure described via CSVW and physical mappings." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "geochem-measurements.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 6249 ] ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 .

<file:///github/workspace/#part-metadata-yaml> a schema1:MediaObject ;
    schema1:about <file:///github/workspace/#part-results-csv> ;
    schema1:description "Metadata sidecar for the results CSV file." ;
    schema1:encodingFormat "application/yaml" ;
    schema1:name "geochem-detailed-metadata.yaml" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 2281 ] .

<file:///github/workspace/#part-method-pdf> a schema1:MediaObject ;
    schema1:description "Method description document for the analysis." ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "analysis-method.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 56062 ] .

<file:///github/workspace/#part-spectra-nc> a cdi:StructuredDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/wavelength" ;
            cdi:physicalDataType "float32" ],
        [ cdi:format "decimal" ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/intensity" ;
            cdi:physicalDataType "float32" ] ;
    schema1:description "Spectral data cube with wavelength and intensity dimensions." ;
    schema1:encodingFormat "application/x-netcdf" ;
    schema1:name "spectra-cube.nc" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 13743003 ] .

ex:complete-dataset-001 a schema1:Dataset ;
    schema1:additionalType "geochemistry analysis" ;
    schema1:conditionsOfAccess "Open access; citation required" ;
    schema1:creator ( <https://orcid.org/0000-0001-2345-6789> ) ;
    schema1:dateModified "2026-02-15" ;
    schema1:datePublished "2026-02-01" ;
    schema1:description "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/geochem-summary.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Geochemistry summary results" ;
            spdx:checksum [ spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ],
        [ a cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:hasPhysicalMapping [ cdi:format "string" ;
                    cdi:formats_InstanceVariable ex:var-sampleID ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:physicalDataType "string" ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-concentration ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "NA" ;
                    cdi:physicalDataType "float64" ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-uncertainty ;
                    cdi:index 2 ;
                    cdi:isRequired false ;
                    cdi:nullSequence "-9999" ;
                    cdi:physicalDataType "float64" ] ;
            cdi:isDelimited true ;
            schema1:contentUrl "https://example.org/data/geochem-detailed.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Detailed geochemistry analysis results" ;
            spdx:checksum [ spdx:algorithm "SHA256" ;
                    spdx:checksumValue "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3" ] ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ],
        [ a cdi:StructuredDataSet,
                schema1:DataDownload ;
            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-wavelength ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:locator "/spectra/wavelength" ;
                    cdi:physicalDataType "float32" ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-intensity ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:locator "/spectra/intensity" ;
                    cdi:physicalDataType "float32" ;
                    cdi:scale 1000 ] ;
            schema1:contentUrl "https://example.org/data/spectra-cube.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Spectral data cube" ;
            spdx:checksum [ spdx:algorithm "SHA256" ;
                    spdx:checksumValue "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4" ] ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/geochem-package.zip" ;
            schema1:description "Archive containing all data files. Component files are listed as parts and are not individually accessible." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#part-measurements-csv>,
                <file:///github/workspace/#part-metadata-yaml>,
                <file:///github/workspace/#part-method-pdf>,
                <file:///github/workspace/#part-results-csv>,
                <file:///github/workspace/#part-spectra-nc> ;
            schema1:name "Complete data package" ;
            spdx:checksum [ spdx:algorithm "SHA256" ;
                    spdx:checksumValue "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5" ] ],
        [ a schema1:WebAPI ;
            schema1:documentation [ a schema1:CreativeWork ;
                    schema1:name "OpenAPI specification for geochemistry data service" ;
                    schema1:url "https://example.org/api/v1/openapi.json" ] ;
            schema1:potentialAction [ a schema1:Action ;
                    schema1:name "Query geochemistry features" ;
                    schema1:object [ a schema1:DataFeed ;
                            schema1:description "Geochemistry observations collection" ] ;
                    schema1:query-input [ a schema1:PropertyValueSpecification ;
                            schema1:description "Response format: csv or geojson" ;
                            schema1:valueName "format" ;
                            schema1:valuePattern "csv|geojson" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Starting index for pagination" ;
                            schema1:valueName "offset" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Maximum number of features to return" ;
                            schema1:valueName "limit" ;
                            schema1:valueRequired false ] ;
                    schema1:result [ a schema1:DataDownload ;
                            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:var-uncertainty ;
                                    cdi:index 1 ;
                                    cdi:isRequired false ;
                                    cdi:physicalDataType "float64" ],
                                [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:var-concentration ;
                                    cdi:index 0 ;
                                    cdi:isRequired true ;
                                    cdi:physicalDataType "float64" ] ;
                            cdi:isDelimited true ;
                            schema1:contentUrl "https://example.org/api/v1/collections/geochem/items?f=csv" ;
                            schema1:encodingFormat "text/csv" ;
                            schema1:name "Geochemistry query results" ;
                            csvw:delimiter "," ;
                            csvw:header true ;
                            csvw:headerRowCount 1 ] ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:contentType "application/geo+json",
                                "text/csv" ;
                            schema1:description "OGC API Features endpoint returning geochemistry observations as CSV" ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID "https://www.ogc.org/standards" ;
                            schema1:url "https://www.ogc.org/standard/ogcapi-features/" ;
                            schema1:value "ogcapi-features-1" ] ;
                    schema1:inDefinedTermSet "https://www.ogc.org/standards" ;
                    schema1:name "OGC API - Features" ;
                    schema1:termCode "ogcapi-features" ] ;
            schema1:termsOfService "Open access, no authentication required" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/021nxhr62> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "NSF award number" ;
                    schema1:url "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932" ;
                    schema1:value "EAR-2026932" ] ;
            schema1:name "Geochemistry Data Infrastructure" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.5880/example.complete.001" ;
            schema1:value "10.5880/example.complete.001" ] ;
    schema1:inLanguage "en" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocabularyserver.com/keyword" ;
                    schema1:url "https://vocabularyserver.com/keyword/spectral-001" ;
                    schema1:value "spectral-001" ] ;
            schema1:inDefinedTermSet "https://vocabularyserver.com/keyword" ;
            schema1:name "spectral analysis" ;
            schema1:termCode "SPECTRAL" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocabularyserver.com/keyword" ;
                    schema1:url "https://vocabularyserver.com/keyword/geochem-001" ;
                    schema1:value "geochem-001" ] ;
            schema1:inDefinedTermSet "https://vocabularyserver.com/keyword" ;
            schema1:name "geochemistry" ;
            schema1:termCode "GEOCHEM" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Multi-technique geochemistry dataset with archive and API access" ;
    schema1:publisher ex:ieda-publisher ;
    schema1:sameAs [ a schema1:PropertyValue ;
            schema1:value "urn:example:geochem:complete-001" ] ;
    schema1:subjectOf ex:metadata-record-001 ;
    schema1:url "https://example.org/datasets/complete-001" ;
    schema1:variableMeasured ex:var-concentration,
        ex:var-intensity,
        ex:var-sampleID,
        ex:var-uncertainty,
        ex:var-wavelength ;
    schema1:version "1.0" .

ex:ieda-catalog a schema1:DataCatalog ;
    schema1:name "IEDA Data Catalog" ;
    schema1:url "https://www.earthchem.org/" .

ex:ieda-publisher a schema1:Organization ;
    schema1:alternateName "Interdisciplinary Earth Data Alliance" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/02fjgr047" ;
            schema1:value "02fjgr047" ] ;
    schema1:name "IEDA" .

ex:metadata-record-001 a schema1:Dataset ;
    dcterms:conformsTo <https://example.org/profiles/CDIFcomplete/v0.1> ;
    schema1:about ex:complete-dataset-001 ;
    schema1:includedInDataCatalog ex:ieda-catalog ;
    schema1:maintainer <https://orcid.org/0000-0001-2345-6789> ;
    schema1:sdDatePublished "2026-02-19" .

<https://ror.org/03m2x1q45> a schema1:Organization ;
    schema1:name "University of Arizona" .

<file:///github/workspace/#part-results-csv> a schema1:MediaObject ;
    schema1:description "Detailed geochemistry analysis results in tabular format." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "geochem-detailed.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10860 ] ;
    spdx:checksum [ spdx:algorithm "SHA256" ;
            spdx:checksumValue "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3" ] .

ex:var-intensity a schema1:PropertyValue ;
    schema1:description "Measured spectral intensity" ;
    schema1:name "Spectral intensity" ;
    schema1:propertyID "urn:example:property:intensity" ;
    schema1:unitText "counts" .

ex:var-sampleID a schema1:PropertyValue ;
    schema1:description "Unique identifier for each sample" ;
    schema1:name "Sample identifier" ;
    schema1:propertyID "urn:example:property:sampleID" .

ex:var-wavelength a schema1:PropertyValue ;
    schema1:description "Spectral wavelength" ;
    schema1:maxValue 2500 ;
    schema1:minValue 200 ;
    schema1:name "Wavelength" ;
    schema1:propertyID "urn:example:property:wavelength" ;
    schema1:unitText "nm" .

<https://orcid.org/0000-0001-2345-6789> a schema1:Person ;
    schema1:affiliation <https://ror.org/03m2x1q45> ;
    schema1:alternateName "J. Smith" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jsmith@arizona.edu" ],
        [ a schema1:ContactPoint ;
            schema1:email "jsmith@arizona.edu" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-2345-6789" ;
            schema1:value "0000-0001-2345-6789" ] ;
    schema1:name "Smith, Jane" .

ex:var-concentration a schema1:PropertyValue ;
    schema1:description "Measured element concentration in parts per million" ;
    schema1:maxValue 5000 ;
    schema1:measurementTechnique "ICP-MS" ;
    schema1:minValue 1e-02 ;
    schema1:name "Element concentration" ;
    schema1:propertyID "urn:example:property:concentration" ;
    schema1:unitCode "59" ;
    schema1:unitText "ppm" .

ex:var-uncertainty a schema1:PropertyValue ;
    schema1:description "2-sigma uncertainty on concentration measurement" ;
    schema1:name "Measurement uncertainty" ;
    schema1:propertyID "urn:example:property:uncertainty" ;
    schema1:unitCode "59" ;
    schema1:unitText "ppm" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF complete metadata schema
description: JSON schema for JSON-LD documents that describe science datasets for
  the CDIF complete profile, combining discovery metadata with data description and
  archive distribution extensions. Extends CDIFDiscovery (cdifMandatory + cdifOptional
  including variableMeasured) with distribution constraints supporting single-file
  DataDownloads with optional tabular/dataCube data description, archive distributions
  with hasPart component files, and WebAPI distributions with potentialAction result
  data description.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDiscovery/schema.yaml
- type: object
  properties:
    schema:distribution:
      type: array
      items:
        anyOf:
        - allOf:
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
          - anyOf:
            - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
            - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
            - {}
        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml
        - allOf:
          - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/webAPI/schema.yaml
          - type: object
            properties:
              schema:potentialAction:
                type: array
                items:
                  type: object
                  properties:
                    schema:result:
                      allOf:
                      - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
                      - anyOf:
                        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
                        - $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
                        - {}
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)
* [schema.org DataDownload](https://schema.org/DataDownload)
* [schema.org WebAPI](https://schema.org/WebAPI)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFcomplete`

