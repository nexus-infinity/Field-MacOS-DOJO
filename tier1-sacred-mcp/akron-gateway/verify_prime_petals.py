#!/usr/bin/env python3
"""
Prime Petal Structure Verification Script
Validates that folders have complete P1-P11 structure with refined symbols
"""

from pathlib import Path
from typing import Dict
import json
import sys


def verify_prime_petal_structure(folder_path: Path) -> bool:
    """
    Verify that folder has complete P1-P11 structure with refined symbols

    Args:
        folder_path: Path to folder to verify

    Returns:
        True if structure is complete, False otherwise
    """
    folder = Path(folder_path)

    if not folder.exists():
        print(f"❌ Folder does not exist: {folder}")
        return False

    if not folder.is_dir():
        print(f"❌ Path is not a directory: {folder}")
        return False

    required_files = [
        "· P1_seed_purpose.txt",
        "△ P3_identity_schema.json",
        "⬠ P5_operational_rules.yaml",
        "⬡ P7_temporal_lifecycle.json",
        "✦ P9_wisdom_synthesis.md",
        "⊞ P11_registry_manifest.json"
    ]

    print(f"\n🔍 Verifying Prime Petal structure in: {folder.name}")
    print(f"   Path: {folder}")
    print(f"\n   Checking for required files:")

    all_present = True
    for required_file in required_files:
        file_path = folder / required_file
        exists = file_path.exists()
        status = "✓" if exists else "✗"
        print(f"   {status} {required_file}")

        if not exists:
            all_present = False

    if all_present:
        print(f"\n✅ Prime Petal structure complete!")

        # Validate P11 registry
        registry_path = folder / "⊞ P11_registry_manifest.json"
        try:
            with open(registry_path, 'r', encoding='utf-8') as f:
                registry = json.load(f)

            print(f"\n   Registry details:")
            print(f"   Symbol: {registry['symbol']}")
            print(f"   Prime Level: {registry['prime_level']}")
            print(f"   Files: {registry['total_files']}")
            print(f"   Subfolders: {registry['total_subfolders']}")
            print(f"   Fractal: {registry['fractal_properties']['self_similar']}")
            print(f"   Version: {registry['folder_metadata'].get('prime_petal_version', 'unknown')}")

            return True
        except Exception as e:
            print(f"\n⚠️  Warning: Could not parse P11 registry: {e}")
            return True  # Still valid if files exist
    else:
        print(f"\n❌ Prime Petal structure incomplete!")
        missing = [f for f in required_files if not (folder / f).exists()]
        print(f"\n   Missing files:")
        for f in missing:
            print(f"   - {f}")
        return False


def verify_recursive(root_path: Path, max_depth: int = 5, current_depth: int = 0) -> Dict[str, bool]:
    """
    Recursively verify Prime Petal structure in folder tree

    Args:
        root_path: Root folder to start verification
        max_depth: Maximum recursion depth
        current_depth: Current recursion level (internal)

    Returns:
        Dictionary mapping folder paths to verification status
    """
    results = {}

    if current_depth > max_depth:
        return results

    root = Path(root_path)
    if not root.exists() or not root.is_dir():
        return results

    # Verify current folder
    results[str(root)] = verify_prime_petal_structure(root)

    # Recurse into subfolders
    try:
        for subfolder in sorted(root.iterdir()):
            if subfolder.is_dir() and not subfolder.name.startswith('.'):
                sub_results = verify_recursive(subfolder, max_depth, current_depth + 1)
                results.update(sub_results)
    except PermissionError:
        print(f"⚠️  Permission denied accessing subfolders of {root}")

    return results


def print_summary(results: Dict[str, bool]):
    """Print summary of verification results"""
    total = len(results)
    valid = sum(1 for v in results.values() if v)
    invalid = total - valid

    print(f"\n" + "="*60)
    print(f"VERIFICATION SUMMARY")
    print(f"="*60)
    print(f"Total folders checked: {total}")
    print(f"✅ Valid Prime Petal structures: {valid}")
    print(f"❌ Invalid/incomplete structures: {invalid}")

    if invalid > 0:
        print(f"\n❌ Invalid folders:")
        for path, is_valid in results.items():
            if not is_valid:
                print(f"   - {path}")


def main():
    """Main entry point for verification script"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Verify Prime Petal structure (P1-P11) in folders"
    )
    parser.add_argument(
        "folder",
        type=str,
        help="Path to folder to verify"
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recursively verify subfolders"
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=5,
        help="Maximum recursion depth (default: 5)"
    )

    args = parser.parse_args()

    folder_path = Path(args.folder).expanduser()

    if args.recursive:
        print(f"🔍 Recursive verification starting from: {folder_path}")
        print(f"   Max depth: {args.max_depth}\n")
        results = verify_recursive(folder_path, max_depth=args.max_depth)
        print_summary(results)

        # Exit with error code if any folders are invalid
        sys.exit(0 if all(results.values()) else 1)
    else:
        is_valid = verify_prime_petal_structure(folder_path)
        sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
