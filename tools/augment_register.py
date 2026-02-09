"""Add resolvedSchema URLs to register.json for profile building blocks."""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTER = REPO_ROOT / "build" / "register.json"
SOURCES = REPO_ROOT / "_sources" / "profiles"


def main():
    with open(REGISTER) as f:
        register = json.load(f)

    base_url = register.get("baseURL", "").rstrip("/")

    for bblock in register.get("bblocks", []):
        item_id = bblock.get("itemIdentifier", "")
        # Extract profile name from identifier
        # e.g. cdif.bbr.metadata.profiles.adaProduct -> adaProduct
        parts = item_id.split(".")
        if "profiles" not in parts:
            continue
        profile_idx = parts.index("profiles")
        if profile_idx + 1 >= len(parts):
            continue
        profile_name = parts[profile_idx + 1]

        resolved_path = SOURCES / profile_name / "resolvedSchema.json"
        if resolved_path.exists():
            url = f"{base_url}/_sources/profiles/{profile_name}/resolvedSchema.json"
            bblock["resolvedSchema"] = url

    with open(REGISTER, "w") as f:
        json.dump(register, f, indent=2, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main()
