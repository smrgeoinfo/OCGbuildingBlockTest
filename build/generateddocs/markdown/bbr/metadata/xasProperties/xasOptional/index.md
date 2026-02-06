
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
type: object
allOf:
- $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/metaMetadata/schema.yaml
- properties:
    dcterms:conformsTo:
      type: array
      items:
        $ref: https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/schemaorgProperties/metaMetadata/schema.yaml#/$defs/conformsTo_item
      minItems: 2
      contains:
        type: object
        properties:
          '@id':
            const: cdif:profile_xasCDIF
        required:
        - '@id'
      minContains: 1
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
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
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

