# OGC Building Blocks Repository

Modular schema components following the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern for the [IEDA Data Submission Portal](https://github.com/smrgeoinfo/IEDADataSubmission). Each building block is a self-contained directory with a JSON Schema, JSON-LD context, metadata, and description. Building blocks compose into profiles that define complete metadata schemas for specific use cases.

For more info see [the OGC Documentation](https://ogcincubator.github.io/bblocks-docs/).

## Schema Pipeline

The schema pipeline transforms modular YAML source schemas into JSON Forms-compatible Draft 7 schemas in two steps, plus an augmentation step for the bblocks-viewer:

```
schema.yaml → resolve_schema.py → resolvedSchema.json → convert_for_jsonforms.py → schema.json
                                                       → augment_register.py → register.json (adds resolvedSchema URLs)
```

### Step 1: Resolve (`resolve_schema.py`)

Recursively resolves all `$ref` references from modular YAML/JSON source schemas into one fully-inlined JSON Schema. Handles relative paths, fragment-only refs (`#/$defs/X`), cross-file fragments, and both YAML/JSON extensions. Optionally flattens `allOf` entries.

```bash
# Resolve a profile by name
python tools/resolve_schema.py adaProduct --flatten-allof -o _sources/profiles/adaProduct/resolvedSchema.json

# Resolve all profiles
for p in adaProduct adaEMPA adaICPMS adaVNMIR adaXRD CDIFDiscovery; do
  python tools/resolve_schema.py $p --flatten-allof -o _sources/profiles/$p/resolvedSchema.json
done

# Resolve an arbitrary schema file
python tools/resolve_schema.py --file path/to/any/schema.yaml
```

**Requirements:** Python 3.6+ with `pyyaml` (`pip install pyyaml`)

### Step 2: Convert for JSON Forms (`convert_for_jsonforms.py`)

Reads `resolvedSchema.json` and converts to JSON Forms-compatible Draft 7:
- Converts `$schema` from Draft 2020-12 to Draft 7
- Simplifies `anyOf` patterns for form rendering
- Converts `contains` → `enum`, `const` → `default`
- Merges technique profile constraints into distribution branches
- Preserves `oneOf` in distribution (3 branches: single file, archive, WebAPI)
- Preserves `anyOf` in fileDetail (technique-specific file type subsets)
- Removes `not` constraints and relaxes `minItems`

```bash
# Convert all profiles
python tools/convert_for_jsonforms.py --all -v

# Convert a single profile
python tools/convert_for_jsonforms.py adaEMPA -v
```

### Step 3: Augment register.json (`augment_register.py`)

Adds `resolvedSchema` URLs to `build/register.json` for each profile building block that has a `resolvedSchema.json` file. This enables the bblocks-viewer's "Resolved (JSON)" button to fetch and display the fully resolved schema (all `$ref` inlined, `allOf` flattened).

```bash
python tools/augment_register.py
```

The `generate-jsonforms` workflow runs this automatically after schema conversion.

## Profiles

| Profile | Description |
|---|---|
| `adaProduct` | Base ADA product metadata — distribution has 3 `oneOf` branches (single file, archive, WebAPI) |
| `adaEMPA` | Electron Microprobe Analysis — constrains component types and fileDetail to EMPA-valid file types |
| `adaXRD` | X-ray Diffraction — constrains to XRD-valid component and file types |
| `adaICPMS` | ICP Mass Spectrometry — constrains to ICP-MS-valid component and file types |
| `adaVNMIR` | Very-Near Mid-IR / FTIR — constrains to VNMIR-valid component and file types |
| `CDIFDiscovery` | CDIF Discovery profile — general-purpose dataset metadata |

See [agents.md](agents.md) for the full building block structure, authoring rules, and composition hierarchy.

## License

This material is based upon work supported by the National Science Foundation (NSF) under awards 2012893, 2012748, and 2012593.
