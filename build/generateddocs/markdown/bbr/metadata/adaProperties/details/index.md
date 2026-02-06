
# Instrument Detail Types (Schema)

`cdif.bbr.metadata.adaProperties.details` *v0.1*

Instrument-specific detail types for ADA analytical techniques

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Instrument Detail Types

Collection of instrument-specific detail types for ADA analytical techniques. These are tightly coupled types that describe component-level metadata for various analytical instruments:

- **basemap_detail** - Basemap images with RGB channels and pixel scaling
- **argt_detail** - ARGT (Argon) document type with phase and isotope analysis
- **dsc_detail** - Differential Scanning Calorimetry heat tabular data
- **empa_detail** - Electron Microprobe Analysis with spectrometer and signal details
- **eairms_detail** - Elemental Analysis Isotope Ratio Mass Spectrometry collection
- **icpoes_detail** - Inductively Coupled Plasma Optical Emission Spectrometry
- **l2ms_detail** - Laser-2 Mass Spectrometry cube data with ionization parameters
- **laf_detail** - Laser Ablation Fluorescence processed/raw data
- **nanoir_detail** - Nano-IR spectroscopy collections with phase analysis
- **nanosims_detail** - Nano Secondary Ion Mass Spectrometry with isotope tracking
- **psfd_detail** - Point Spread Function Data with image names and conditions
- **vnmir_detail** - Very-Near Mid-IR spectroscopy with detailed measurement parameters
- **qris_detail** - QRIS (Raman) with calibration and illumination parameters
- **slsshapemodel_detail** - Structured Light Scanning shape models and partial scans
- **xctimage_detail** - X-ray Computed Tomography images with detailed scan parameters
- **xrd_detail** - X-ray Diffraction tabular data with geometry and wavelength

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Instrument Detail Types
description: Collection of instrument-specific detail types for ADA analytical techniques.
  These are tightly coupled types kept together as local definitions.
type: object
anyOf:
- $ref: '#/$defs/basemap_detail'
- $ref: '#/$defs/argt_detail'
- $ref: '#/$defs/dsc_detail'
- $ref: '#/$defs/empa_detail'
- $ref: '#/$defs/eairms_detail'
- $ref: '#/$defs/icpoes_detail'
- $ref: '#/$defs/l2ms_detail'
- $ref: '#/$defs/laf_detail'
- $ref: '#/$defs/nanoir_detail'
- $ref: '#/$defs/nanosims_detail'
- $ref: '#/$defs/psfd_detail'
- $ref: '#/$defs/vnmir_detail'
- $ref: '#/$defs/qris_detail'
- $ref: '#/$defs/slsshapemodel_detail'
- $ref: '#/$defs/xctimage_detail'
- $ref: '#/$defs/xrd_detail'
$defs:
  basemap_detail:
    type: object
    description: Basemap images with RGB channels and pixel scaling.
    properties:
      '@type':
        const:
        - ada:basemap
        - schema:Map
      schema:description:
        type: string
      pixelUnits:
        type: string
      pixelScaleX:
        type: number
      pixelScaleY:
        type: number
      channel1:
        type: string
      channel2:
        type: string
      channel3:
        type: string
    required:
    - '@type'
    - pixelScaleX
    - pixelScaleY
    - pixelUnits
  argt_detail:
    type: object
    description: ARGT (Argon) document type with phase and isotope analysis
    properties:
      '@type':
        const:
        - ada:ARGTDocument
      phaseAnalyzed:
        type: string
      isotopeType:
        type: string
  dsc_detail:
    type: object
    description: Differential Scanning Calorimetry heat tabular data
    properties:
      '@type':
        const:
        - ada:DSCHeatTabular
      analysisType:
        type: string
  empa_detail:
    type: object
    description: Electron Microprobe Analysis with spectrometer and signal details.
    properties:
      '@type':
        anyOf:
        - const:
          - ada:EMPAImage
        - const:
          - ada:EMPAQEATabular
        - const:
          - ada:EMPAImageCollection
      spectrometersUsed:
        type: string
        description: Spectrometers used in analysis
      signalUsed:
        type: string
  eairms_detail:
    type: object
    description: Elemental Analysis Isotope Ratio Mass Spectrometry collection
    properties:
      '@type':
        const:
        - ada:EAIRMSCollection
      massConsumed:
        type: string
      elementType:
        type: string
  icpoes_detail:
    type: object
    description: Inductively Coupled Plasma Optical Emission Spectrometry
    properties:
      '@type':
        anyOf:
        - const:
          - ada:ICPOESIntermediateTabular
        - const:
          - ada:ICPOESProcessedTabular
        - const:
          - ada:ICPOESRawTabular
      mass:
        type: string
      dissolutionFactor:
        type: number
  l2ms_detail:
    type: object
    description: Laser-2 Mass Spectrometry cube data with ionization parameters
    properties:
      '@type':
        const:
        - ada:L2MSCube
      sampleName:
        type: string
      ionizationTimeDelay:
        type: integer
      massGate:
        type: boolean
      photoionizationWavelength:
        type: integer
      plasmaShutter:
        type: boolean
      timeDelayUnits:
        type: string
      wavelengthUnits:
        type: string
  laf_detail:
    type: object
    description: Laser Ablation Fluorescence processed/raw data. elementAnalyzed goes
      in resultTarget.
    properties:
      '@type':
        anyOf:
        - const:
          - ada:LAFProcessed
        - const:
          - ada:LAFRaw
      elementAnalyzed:
        type: string
      sampleMassConsumed:
        type: string
      sampleType:
        type: string
  nanoir_detail:
    type: object
    description: Nano-IR spectroscopy collections with phase analysis
    properties:
      '@type':
        anyOf:
        - const:
          - ada:NanoIRBackground
        - const:
          - ada:NanoIRMapCollection
        - const:
          - ada:NanoIRPointCollection
      phaseAnalyzed:
        type: array
        minItems: 0
        items:
          type: string
  nanosims_detail:
    type: object
    description: Nano Secondary Ion Mass Spectrometry with isotope tracking
    properties:
      '@type':
        anyOf:
        - const:
          - ada:NanoSIMSCollection
        - const:
          - ada:NanoSIMSImageCollection
        - const:
          - ada:NanoSIMSTabular
        - const:
          - ada:NanoSIMSMap
      phaseAnalyzed:
        type: array
        minItems: 0
        items:
          type: string
      isotopeAnalyzed:
        type: array
        minItems: 0
        items:
          type: string
  psfd_detail:
    type: object
    description: Point Spread Function Data with image names and conditions
    properties:
      '@type':
        const:
        - ada:PSFDTabular
      imageName:
        type: array
        minItems: 0
        items:
          type: string
      imageViewingConditions:
        type: string
  vnmir_detail:
    type: object
    description: Very-Near Mid-IR spectroscopy with detailed measurement parameters
    properties:
      '@type':
        anyOf:
        - const:
          - ada:VNMIRSpectralPoint
        - const:
          - ada:VNMIROverviewImage
        - const:
          - ada:VNMIRSpectralMap
      detector:
        type: string
      beamsplitter:
        type: string
      calibrationStandards:
        type: string
      comments:
        type: string
      numberOfScans:
        type: integer
      eMaxFitRegionMax:
        type: string
      eMaxFitRegionMin:
        type: string
      emissionAngle:
        type: number
      emissivityMaximum:
        type: string
      environmentalPressure:
        type: number
      incidenceAngle:
        type: number
      measurement:
        type: string
      measurementEnvironment:
        type: string
      phaseAngle:
        type: number
      sampleHeated:
        type: boolean
      samplePreparation:
        type: string
      sampleTemperature:
        type: integer
      spectralRangeMax:
        type: string
      spectralRangeMin:
        type: string
      spectralResolution:
        type: string
      spectralSampling:
        type: string
      spotSize:
        type: string
      uncertaintyNoise:
        type: number
      vacuumExposedSample:
        type: boolean
  qris_detail:
    type: object
    description: QRIS (Raman) with calibration and illumination parameters
    properties:
      '@type':
        anyOf:
        - const:
          - ada:QRISCalibrated
        - const:
          - ada:QRISRaw
      calibrationFile:
        type: string
      pipelineVersion:
        type: string
      focalLength:
        type: integer
      illuminationColor:
        type: array
        minItems: 0
        items:
          type: string
      illuminationLevel:
        type: integer
      exposureTime:
        type: integer
      target:
        type: string
  slsshapemodel_detail:
    type: object
    description: Structured Light Scanning shape models and partial scans
    properties:
      '@type':
        anyOf:
        - const:
          - ada:SLSShapeModel
        - const:
          - ada:SLSPartialScan
      countScans:
        type: integer
      facets:
        type: integer
      unitsOfMeasurement:
        type: string
      version:
        type: integer
      vertices:
        type: integer
      watertight:
        type: boolean
  xctimage_detail:
    type: object
    description: X-ray Computed Tomography images with detailed scan parameters
    properties:
      '@type':
        const:
        - ada:XCTImageCollection
      beamFilterMaterial:
        type: string
      beamFilterThickness:
        type: number
      dataRangeLower:
        type: integer
      dataRangeUpper:
        type: integer
      detectorGain:
        type: string
      detectorBinning:
        type: string
      detectorSize:
        type: string
      detectorType:
        type: string
      imageExposure:
        type: number
      imageFPS:
        type: string
      imageGain:
        type: number
      imageSize:
        type: string
      instrumentType:
        type: string
      nsiBeamHardening:
        type: number
      numberOfFramesAveragedPerProjection:
        type: integer
      numberOfProjections:
        type: integer
      numberOfSlices:
        type: integer
      pixelPitch:
        type: string
      reconstructedDataFormat:
        type: string
      reconstructedVoxelSize:
        type: string
      reconstructionSoftware:
        type: string
      rotationAngle:
        type: string
      rotationType:
        type: string
      sourceToDetectorDistance:
        type: string
      sourceToObjectDistance:
        type: number
      subPixGrid:
        type: string
      subPixShift:
        type: string
      xraySource:
        type: string
      xrayTargetMaterial:
        type: string
      xrayTubeCurrent:
        type: number
      xrayTubeEnergy:
        type: number
      xrayTubePower:
        type: number
  xrd_detail:
    type: object
    description: X-ray Diffraction tabular data with geometry and wavelength
    properties:
      '@type':
        const:
        - ada:XRDTabular
      geometry:
        type: string
      sampleMount:
        type: string
      stepSize:
        type: number
      timePerStep:
        type: number
      wavelength:
        type: number
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.json)
* JSON version: [schema.json](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://smrgeoinfo.github.io/OCGbuildingBlockTest/build/annotated/bbr/metadata/adaProperties/details/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/smrgeoinfo/OCGbuildingBlockTest](https://github.com/smrgeoinfo/OCGbuildingBlockTest)
* Path: `_sources/adaProperties/details`

