#!/usr/bin/env python3
"""
Batch Prime Petal Generator
Recursively generates Prime Petal structures across folder trees
"""

import os
from pathlib import Path
from prime_petal_generator import RefinedPrimePetalGenerator
import argparse


def generate_recursive_prime_petals(
    root_path: Path,
    max_depth: int = 10,
    skip_existing: bool = True,
    context_generator=None
):
    """
    Walk folder tree and generate Prime Petals in each folder

    Args:
        root_path: Root directory to start from
        max_depth: Maximum depth to traverse
        skip_existing: Skip folders that already have P11 manifest
        context_generator: Optional function to generate context for each folder
    """
    generator = RefinedPrimePetalGenerator()
    processed = 0
    skipped = 0

    print(f"\n🌸 Batch Prime Petal Generation")
    print(f"   Root: {root_path}")
    print(f"   Max Depth: {max_depth}")
    print(f"   Skip Existing: {skip_existing}")
    print(f"\n{'='*60}\n")

    for dirpath, dirnames, filenames in os.walk(root_path):
        folder = Path(dirpath)

        # Calculate current depth
        try:
            relative = folder.relative_to(root_path)
            depth = len(relative.parts)
        except ValueError:
            depth = 0

        if depth > max_depth:
            # Don't recurse deeper
            dirnames.clear()
            continue

        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        # Check if already has P11 manifest
        manifest_exists = (folder / "⊞ P11_registry_manifest.json").exists()

        if manifest_exists and skip_existing:
            print(f"   ⏭️  Skipping {folder.name} (depth {depth}) - already has Prime Petals")
            skipped += 1
            continue

        # Generate context for this folder
        context = None
        if context_generator:
            context = context_generator(folder)

        # Generate Prime Petals
        try:
            generator.generate_prime_structure(
                folder_path=folder,
                purpose=f"Recursive Prime Petal generation for {folder.name}",
                context=context
            )
            processed += 1
        except Exception as e:
            print(f"   ❌ Error processing {folder}: {e}")

    print(f"\n{'='*60}")
    print(f"✅ Batch generation complete!")
    print(f"   Processed: {processed} folders")
    print(f"   Skipped: {skipped} folders")
    print(f"   Total: {processed + skipped} folders")


def generate_context_from_path(folder: Path) -> dict:
    """
    Generate context dictionary from folder path analysis

    Args:
        folder: Path to analyze

    Returns:
        Context dictionary with inferred metadata
    """
    context = {
        "type": "auto_generated",
        "depth": len(folder.parts),
        "parent": str(folder.parent.name)
    }

    name_lower = folder.name.lower()

    # Infer case ID if present
    if "case" in name_lower:
        # Try to extract case number
        import re
        case_match = re.search(r'case[_-]?(\w+)', name_lower)
        if case_match:
            context['case_id'] = f"case_{case_match.group(1)}"

    # Infer folder type
    if "evidence" in name_lower:
        context['type'] = "evidence_archive"
    elif "contract" in name_lower:
        context['type'] = "legal_contracts"
    elif "email" in name_lower or "communication" in name_lower:
        context['type'] = "communications"
    elif "knowledge" in name_lower or "research" in name_lower:
        context['type'] = "knowledge_base"

    return context


def main():
    """Main entry point for batch generation"""
    parser = argparse.ArgumentParser(
        description="Batch generate Prime Petal structures across folder trees"
    )
    parser.add_argument(
        "root",
        type=str,
        help="Root directory to start from"
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=10,
        help="Maximum folder depth to traverse (default: 10)"
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="Don't skip folders that already have Prime Petals"
    )
    parser.add_argument(
        "--auto-context",
        action="store_true",
        help="Auto-generate context from folder paths"
    )

    args = parser.parse_args()

    root_path = Path(args.root).expanduser().resolve()

    if not root_path.exists():
        print(f"❌ Error: Root path does not exist: {root_path}")
        return 1

    if not root_path.is_dir():
        print(f"❌ Error: Root path is not a directory: {root_path}")
        return 1

    context_gen = generate_context_from_path if args.auto_context else None

    generate_recursive_prime_petals(
        root_path=root_path,
        max_depth=args.max_depth,
        skip_existing=not args.no_skip,
        context_generator=context_gen
    )

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
