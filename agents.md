# JSON Schema Reference Resolver

## Overview

The `resolve_schema.py` script is a Python utility that transforms modular OGC Building Block JSON schemas into standalone, self-contained schemas. It recursively resolves all external `$ref` references and flattens definitions into a single `$defs` section.

## Purpose

OGC Building Blocks use a modular architecture where schemas reference each other using JSON Schema's `$ref` keyword. While this modularity is excellent for maintenance and reusability, some tools and validators require fully resolved, standalone schemas. This tool bridges that gap.

### Before (Modular)
```json
{
  "$defs": {
    "Person": {"$ref": "../person/personSchema.json"},
    "Organization": {"$ref": "../organization/organizationSchema.json"}
  }
}
```

### After (Standalone)
```json
{
  "$defs": {
    "Person": { /* full person schema inlined */ },
    "Organization": { /* full organization schema inlined */ }
  }
}
```

## Installation

No external dependencies required. The script uses only Python standard library modules:
- `json` - JSON parsing and serialization
- `pathlib` - Cross-platform path handling
- `argparse` - Command-line argument parsing
- `copy` - Deep copying of schema objects
- `urllib.parse` - URL fragment parsing

**Requirements:** Python 3.6+

## Usage

### Basic Usage

```bash
# Print resolved schema to stdout
python resolve_schema.py <input_schema_path>

# Save to file
python resolve_schema.py <input_schema_path> -o <output_path>
```

### Examples

```bash
# Resolve the main CDIF Discovery profile
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json

# Save resolved schema to a file
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json -o resolved_cdif.json

# Verbose mode - shows which files are being loaded
python resolve_schema.py _sources/schemaorgProperties/cdifMandatory/cdifMandatorySchema.json -v

# Custom JSON indentation (default is 2)
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json --indent 4
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `input_schema` | Path to the input JSON schema file (required) |
| `-o, --output` | Output file path (default: prints to stdout) |
| `-v, --verbose` | Print progress information to stderr |
| `--indent` | JSON indentation level (default: 2) |
| `--inline-single-use` | Inline definitions that are only referenced once |

## How It Works

### Architecture

The resolver uses a single-pass recursive algorithm with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     SchemaResolver                          │
├─────────────────────────────────────────────────────────────┤
│  schema_cache      Dict[str, dict]   Loaded file cache      │
│  global_defs       Dict[str, dict]   Flattened definitions  │
│  processing_stack  Set[str]          Cycle detection        │
│  file_to_def_name  Dict[str, str]    Path → def name map    │
│  warnings          List[str]         Collected warnings     │
└─────────────────────────────────────────────────────────────┘
```

### Processing Flow

```
1. Load root schema
       │
       ▼
2. Process schema recursively
       │
       ├──► Find $ref → External? ──► Load & process referenced file
       │                    │              │
       │                    │              ▼
       │                    │         Add to global_defs
       │                    │              │
       │                    │              ▼
       │                    └──────► Replace with #/$defs/Name
       │
       ├──► Find $defs → Process each definition
       │                    │
       │                    ▼
       │              Add to global_defs (flattened)
       │
       └──► Process nested objects/arrays recursively
       │
       ▼
3. Merge global_defs into result
       │
       ▼
4. Output standalone schema
```

### Reference Types Handled

The resolver handles all common JSON Schema reference patterns:

| Pattern | Example | Description |
|---------|---------|-------------|
| Relative file | `"$ref": "../person/personSchema.json"` | Reference to another schema file |
| Fragment | `"$ref": "#/$defs/Identifier"` | Internal reference (preserved as-is) |
| File + Fragment | `"$ref": "../file.json#/$defs/Name"` | Reference to specific definition in another file |
| allOf composition | `"allOf": [{"$ref": "..."}]` | Schema composition |

### Key Methods

#### `resolve(schema_path: str) -> dict`
Main entry point. Loads the root schema and initiates processing.

```python
resolver = SchemaResolver(verbose=True)
result = resolver.resolve("path/to/schema.json")
```

#### `process_schema(schema: Any, current_dir: Path) -> Any`
Recursively processes a schema node, handling:
- `$ref` references (external → resolved, internal → preserved)
- `$defs` sections (extracted and flattened)
- Nested objects and arrays

#### `get_or_create_def_for_file(schema_path: Path, fragment: Optional[str]) -> str`
Ensures each external schema is processed only once:
1. Checks cache for existing definition
2. Generates unique name if needed
3. Loads and processes the schema
4. Stores in `global_defs`
5. Returns the definition name

#### `parse_ref(ref: str) -> Tuple[str, Optional[str]]`
Splits a `$ref` value into file path and fragment:
```python
parse_ref("../person/personSchema.json#/$defs/Name")
# Returns: ("../person/personSchema.json", "/$defs/Name")
```

## Features

### Caching
Schemas are loaded once and cached. If multiple schemas reference the same file, it's only read from disk once.

### Cycle Detection
The `processing_stack` tracks schemas currently being processed. If a cycle is detected, the resolver returns a reference to the existing definition instead of infinite recursion.

### Unique Name Generation
When multiple schemas define types with the same name, the resolver generates unique names:
```
Person, Person_2, Person_3, ...
```

### Typo Detection
The resolver detects common typos like using `"$defs"` instead of `"$ref"`:
```json
// This typo is detected and handled:
{"$defs": "../variableMeasured/variableMeasuredSchema.json"}
// Should be:
{"$ref": "../variableMeasured/variableMeasuredSchema.json"}
```

A warning is emitted but processing continues.

### Property Preservation
When a `$ref` has sibling properties (uncommon but valid), they are preserved:
```json
// Input
{"$ref": "../identifier/identifierSchema.json", "description": "Custom desc"}

// Output
{"$ref": "#/$defs/Identifier", "description": "Custom desc"}
```

### Inline Single-Use Definitions

With the `--inline-single-use` flag, the resolver produces a more compact schema by:
1. Keeping definitions in `$defs` only if they are referenced multiple times
2. Inlining definitions that are referenced only once directly where they are used

This produces output similar to hand-authored schemas like `CDIF-JSONLD-schema-schemaprefix.json`.

```bash
python resolve_schema.py schema.json -o output.json --inline-single-use -v
```

Example output (verbose mode):
```
Single-use definitions to inline: {'DataDownload', 'MetaMetadata', 'WebAPI', ...}
Multi-use definitions to keep: {'Person', 'Organization', 'Identifier', 'DefinedTerm', ...}
```

The optimization considers:
- References in the main schema properties
- References within other definitions (if A references B multiple times, B is kept in `$defs`)
- Unreferenced definitions are also inlined (they may be dead code)

## Output Format

The resolved schema has all definitions in a single top-level `$defs` section:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "creator": {"$ref": "#/$defs/Person"}
  },
  "$defs": {
    "Person": { /* ... */ },
    "Organization": { /* ... */ },
    "Identifier": { /* ... */ }
  }
}
```

All external references are converted to internal references:
- Before: `{"$ref": "../person/personSchema.json"}`
- After: `{"$ref": "#/$defs/Person"}`

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `Input file not found` | Schema path doesn't exist | Check the path |
| `Referenced file not found` | A `$ref` points to non-existent file | Fix the reference path |
| `Invalid JSON` | Malformed JSON in a schema file | Fix the JSON syntax |
| `Missing key` | Fragment references non-existent path | Fix the fragment pointer |

Use `-v` (verbose) mode to see the full stack trace for debugging.

## Limitations

1. **HTTP/HTTPS references**: Only local file references are supported. Remote URLs in `$ref` are not fetched.

2. **JSON Schema keywords**: The resolver doesn't validate JSON Schema semantics; it only resolves references.

3. **Circular references**: While detected, complex circular dependencies may result in incomplete definitions.

## Example: Building Block Structure

The resolver is designed for the OGC Building Blocks directory structure:

```
_sources/
├── profiles/
│   └── CDIFDiscovery/
│       └── CDIFDiscoverySchema.json    ← Profile (uses allOf)
├── schemaorgProperties/
│   ├── person/
│   │   └── personSchema.json           ← Component
│   ├── organization/
│   │   └── organizationSchema.json     ← Component
│   └── identifier/
│       └── identifierSchema.json       ← Component
└── provProperties/
    └── generatedBy/
        └── generatedBySchema.json      ← Component
```

Running on the profile:
```bash
python resolve_schema.py _sources/profiles/CDIFDiscovery/CDIFDiscoverySchema.json -v
```

Output shows the dependency resolution:
```
Loading: .../CDIFDiscoverySchema.json
Loading: .../cdifMandatorySchema.json
Loading: .../personSchema.json
Loading: .../organizationSchema.json
Loading: .../identifierSchema.json
...
```

## Programmatic Usage

The resolver can be used as a library:

```python
from resolve_schema import SchemaResolver

# Create resolver
resolver = SchemaResolver(verbose=False)

# Resolve schema
standalone_schema = resolver.resolve("path/to/schema.json")

# Check for warnings
if resolver.warnings:
    print("Warnings:", resolver.warnings)

# Use the resolved schema
import json
print(json.dumps(standalone_schema, indent=2))
```

## Contributing

When modifying the resolver:

1. Test with simple schemas first (e.g., `identifierSchema.json`)
2. Test with complex profiles (e.g., `CDIFDiscoverySchema.json`)
3. Verify no external references remain: `grep '"$ref"' output.json | grep -v '#/$defs/'`
4. Validate the output is valid JSON

## License

This tool is part of the OGC Building Blocks repository. See the repository license for terms.
