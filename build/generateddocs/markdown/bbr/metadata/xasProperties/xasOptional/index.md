
# Optional Fields for XAS data (Schema)

`cdif.bbr.metadata.xasProperties.xasOptional` *v0.1*

XAS profile files that provide additional useful information

[*Status*](http://www.opengis.net/def/status): Under development

## Description

##  XAS profile extension properties

XAS profile files that extend requirements of CDIF discovery. Field content: x-ray source,definition, Data/mode, element/symbol, edge,Instrument/source/type, Instrument/source/name, Instrument/source/probe, Instrument/monochromator/type, Instrument/monochromator/d_spacing, Instrument/monochromator/reflection, Sample/name
## Examples

### Example XAS metadata conforms to extension.
Import base schema.org SubjectOf, add requiremnet that dcterms:conformsTo has XAS profile URI.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: '#/$defs/CdifMandatory'
- type: object
  properties:
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
      allOf:
      - contains:
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
      allOf:
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
          required:
          - schema:inDefinedTermSet
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: http://sweetontology.net/matrElement
          required:
          - schema:inDefinedTermSet
$defs:
  CdifMandatory:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/schemaorgProperties/cdifMandatory/cdifMandatorySchema.json
  DefinedTerm:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/schemaorgProperties/definedTerm/definedTermSchema.json
  AdditionalProperty:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/schemaorgProperties/additionalProperty/additionalPropertySchema.json
  DataDownload:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/schemaorgProperties/dataDownload/dataDownloadSchema.json
  XasSample:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/xasProperties/xasSample/xasSampleSchema.json
  XasSubject:
    $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/_sources/xasProperties/xasSubject/xasSubjectSchema.json
x-jsonld-extra-terms:
  schema: https://schema.org

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasOptional/schema.yaml)


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
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/xasProperties/xasOptional/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/xasProperties/xasOptional`

