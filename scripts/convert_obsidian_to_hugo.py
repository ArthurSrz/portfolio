#!/usr/bin/env python3
"""
Obsidian to Hugo Constellation Converter

Converts Obsidian portfolio markdown files to Hugo constellation format.
Handles:
- Frontmatter conversion
- [[wikilinks]] extraction
- ![[image]] syntax conversion
- Parent-child relationship mapping
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# Paths
OBSIDIAN_ROOT = Path(__file__).parent.parent.parent  # portfolio/
HUGO_ROOT = Path(__file__).parent.parent  # hugo-site/
CONTENT_DIR = HUGO_ROOT / "content" / "nodes"
STATIC_DIR = HUGO_ROOT / "static" / "images"

# Shape mapping by node type
SHAPE_MAP = {
    "person": "circle",
    "category": "pentagon",
    "experience": "square",
    "employer": "hexagon",
    "prototype": "diamond",
    "subcomponent": "triangle",
}

# Track all created nodes for validation
created_nodes = []


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    # Remove parentheses and their contents for cleaner slugs
    text = re.sub(r'\s*\([^)]*\)', '', text)
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body content."""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()

    # Simple YAML parsing (handles our specific format)
    frontmatter = {}
    current_key = None
    current_list = None

    for line in frontmatter_text.split('\n'):
        line = line.rstrip()
        if not line:
            continue

        # Check for list item
        if line.startswith('  - '):
            if current_key and current_list is not None:
                value = line[4:].strip().strip('"')
                current_list.append(value)
            continue

        # Check for key: value
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"')

            if not value:  # Start of a list
                current_key = key
                current_list = []
                frontmatter[key] = current_list
            else:
                frontmatter[key] = value
                current_key = None
                current_list = None

    return frontmatter, body


def extract_wikilink(text: str) -> str:
    """Extract text from [[wikilink]] format."""
    match = re.search(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text)
    if match:
        return match.group(1)
    return text


def convert_image_syntax(content: str) -> str:
    """Convert Obsidian ![[image]] to Hugo markdown."""
    def replace_image(match):
        filename = match.group(1)
        return f'![{filename}](/images/{filename})'

    # Pattern: ![[filename.ext|alignment|size]]
    pattern = r'!\[\[([^\]|]+)(?:\|[^\]]+)*\]\]'
    return re.sub(pattern, replace_image, content)


def clean_content(content: str) -> str:
    """Clean Obsidian-specific syntax for Hugo."""
    # Convert images first
    content = convert_image_syntax(content)

    # Convert [[wikilinks]] to plain text (keep the text, remove brackets)
    content = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',
                     lambda m: m.group(2) or m.group(1), content)

    # Remove dataview blocks
    content = re.sub(r'```dataview[\s\S]*?```', '', content)

    return content.strip()


def build_subtitle(frontmatter: dict, node_type: str) -> str:
    """
    Build a subtitle for the node.

    USER CONTRIBUTION OPPORTUNITY:
    This function determines how each node's summary appears.
    Consider: dates, status, type, or a combination.

    Current implementation: Shows date range and status.
    """
    parts = []

    # Date range
    start = frontmatter.get('start_date', '')
    end = frontmatter.get('end_date', '')
    if start:
        if isinstance(start, datetime):
            start = start.strftime('%Y')
        else:
            start = str(start)[:4]  # Get year
        if end:
            if isinstance(end, datetime):
                end = end.strftime('%Y')
            else:
                end = str(end)[:4]
            parts.append(f"{start}-{end}")
        else:
            parts.append(f"{start}-present")

    # Status
    status = frontmatter.get('status', [])
    if isinstance(status, list) and status:
        status = status[0]
    if status:
        parts.append(status)

    # Type for prototypes
    if node_type in ('prototype', 'subcomponent'):
        node_types = frontmatter.get('type', [])
        if isinstance(node_types, list) and node_types:
            parts.append(node_types[0])

    return ' | '.join(parts) if parts else ''


def build_connection_label(frontmatter: dict) -> str:
    """Build connection label from employer or experience."""
    # Try employer first
    employers = frontmatter.get('employer', [])
    if isinstance(employers, list) and employers:
        return extract_wikilink(employers[0])

    # Try experience
    experiences = frontmatter.get('experience', [])
    if isinstance(experiences, list) and experiences:
        return extract_wikilink(experiences[0])

    return ''


def write_hugo_node(
    node_id: str,
    title: str,
    node_type: str,
    parent: str = None,
    subtitle: str = '',
    content: str = '',
    connection_label: str = '',
    weight: int = 10
):
    """Write a Hugo node markdown file."""
    shape = SHAPE_MAP.get(node_type, 'square')

    # Build frontmatter
    fm_lines = [
        '---',
        f'title: "{title}"',
        'type: "nodes"',
        f'id: "{node_id}"',
        f'shape: "{shape}"',
    ]

    if parent:
        fm_lines.append(f'parent: "{parent}"')
    if subtitle:
        fm_lines.append(f'subtitle: "{subtitle}"')
    if connection_label:
        fm_lines.append(f'connectionLabel: "{connection_label}"')

    fm_lines.extend([
        'connectionType: "solid"',
        f'weight: {weight}',
        'draft: false',
        '---',
    ])

    file_content = '\n'.join(fm_lines)
    if content:
        file_content += f'\n\n{content}'

    # Write file
    filepath = CONTENT_DIR / f'{node_id}.md'
    filepath.write_text(file_content, encoding='utf-8')
    created_nodes.append(node_id)
    print(f"  Created: {node_id}.md ({node_type})")


def create_person_node():
    """Create the center node for Arthur Sarazin."""
    print("\n[Creating person node]")
    write_hugo_node(
        node_id='person',
        title='Arthur Sarazin',
        node_type='person',
        subtitle='Data Product Designer & Researcher',
        content='''I design and build data products that bridge the gap between complex data systems and human understanding.

My work spans frameworks, applications, and research tools - always with a focus on making data accessible and actionable.

Explore the constellation to discover my projects, collaborations, and professional journey.''',
        weight=1
    )


def create_category_nodes():
    """Create category nodes that branch from person."""
    print("\n[Creating category nodes]")
    categories = [
        ('experiences', 'Experiences', 'Professional roles and expertise areas'),
        ('employers', 'Employers', 'Organizations I have worked with'),
        ('prototypes', 'Prototypes', 'Data products, tools, and frameworks'),
    ]

    for cat_id, title, description in categories:
        write_hugo_node(
            node_id=cat_id,
            title=title,
            node_type='category',
            parent='person',
            subtitle=description,
            weight=2
        )


def convert_experience_files():
    """Convert experience folder files."""
    print("\n[Converting experience files]")
    experience_dir = OBSIDIAN_ROOT / 'experience'

    if not experience_dir.exists():
        print("  Warning: experience directory not found")
        return

    for filepath in experience_dir.glob('*.md'):
        filename = filepath.stem
        node_id = slugify(filename)

        content = filepath.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        write_hugo_node(
            node_id=node_id,
            title=filename,
            node_type='experience',
            parent='experiences',
            subtitle=build_subtitle(frontmatter, 'experience'),
            content=clean_content(body) if body else '',
            weight=10
        )


def convert_employer_files():
    """Convert employer folder files."""
    print("\n[Converting employer files]")
    employer_dir = OBSIDIAN_ROOT / 'employer'

    if not employer_dir.exists():
        print("  Warning: employer directory not found")
        return

    for filepath in employer_dir.glob('*.md'):
        filename = filepath.stem
        # Clean up filename (remove parenthetical notes)
        clean_name = re.sub(r'\s*\([^)]*\)', '', filename).strip()
        node_id = slugify(filename)

        content = filepath.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        write_hugo_node(
            node_id=node_id,
            title=clean_name,
            node_type='employer',
            parent='employers',
            subtitle=build_subtitle(frontmatter, 'employer'),
            content=clean_content(body) if body else '',
            weight=10
        )


def convert_prototype_files():
    """Convert prototype files (both root-level and in subdirectories)."""
    print("\n[Converting prototype files]")
    prototypes_dir = OBSIDIAN_ROOT / 'prototypes'

    if not prototypes_dir.exists():
        print("  Warning: prototypes directory not found")
        return

    # First pass: root-level .md files (main prototypes)
    for filepath in prototypes_dir.glob('*.md'):
        convert_single_prototype(filepath, is_subcomponent=False)

    # Second pass: subdirectories (parent + subcomponents)
    for subdir in prototypes_dir.iterdir():
        if subdir.is_dir() and not subdir.name.startswith('.'):
            # Find the parent file (matches directory name)
            parent_file = subdir / f'{subdir.name}.md'

            for filepath in subdir.glob('*.md'):
                is_parent = filepath.name == f'{subdir.name}.md'
                convert_single_prototype(
                    filepath,
                    is_subcomponent=not is_parent,
                    parent_dir_name=subdir.name if not is_parent else None
                )


def convert_single_prototype(filepath: Path, is_subcomponent: bool, parent_dir_name: str = None):
    """Convert a single prototype or subcomponent file."""
    filename = filepath.stem
    node_id = slugify(filename)

    content = filepath.read_text(encoding='utf-8')
    frontmatter, body = extract_frontmatter(content)

    # Determine parent
    if is_subcomponent:
        # Check for explicit prototype reference in frontmatter
        prototype_ref = frontmatter.get('prototype', '')
        if prototype_ref:
            parent = slugify(extract_wikilink(prototype_ref))
        elif parent_dir_name:
            parent = slugify(parent_dir_name)
        else:
            parent = 'prototypes'
        node_type = 'subcomponent'
    else:
        parent = 'prototypes'
        node_type = 'prototype'

    write_hugo_node(
        node_id=node_id,
        title=filename,
        node_type=node_type,
        parent=parent,
        subtitle=build_subtitle(frontmatter, node_type),
        content=clean_content(body) if body else '',
        connection_label=build_connection_label(frontmatter),
        weight=10 if node_type == 'prototype' else 20
    )


def copy_media_files():
    """Copy media files to static directory."""
    print("\n[Copying media files]")
    media_dir = OBSIDIAN_ROOT / 'media'

    if not media_dir.exists():
        print("  Warning: media directory not found")
        return

    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    for filepath in media_dir.glob('*'):
        if filepath.is_file() and not filepath.name.startswith('.'):
            dest = STATIC_DIR / filepath.name
            shutil.copy2(filepath, dest)
            print(f"  Copied: {filepath.name}")


def validate_graph():
    """Validate that all nodes have valid parent connections."""
    print("\n[Validating graph structure]")

    orphans = []
    for node_id in created_nodes:
        if node_id == 'person':
            continue  # Center node has no parent

        filepath = CONTENT_DIR / f'{node_id}.md'
        content = filepath.read_text(encoding='utf-8')

        # Check for parent in frontmatter
        if 'parent:' not in content:
            orphans.append(node_id)

    if orphans:
        print(f"  Warning: Found {len(orphans)} orphan nodes: {orphans}")
    else:
        print(f"  All {len(created_nodes)} nodes are connected")


def main():
    """Main conversion process."""
    print("=" * 60)
    print("Obsidian to Hugo Constellation Converter")
    print("=" * 60)

    # Ensure content directory exists
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Create structure nodes
    create_person_node()
    create_category_nodes()

    # Step 2: Convert content files
    convert_experience_files()
    convert_employer_files()
    convert_prototype_files()

    # Step 3: Copy media
    copy_media_files()

    # Step 4: Validate
    validate_graph()

    print("\n" + "=" * 60)
    print(f"Conversion complete! Created {len(created_nodes)} nodes.")
    print(f"Content directory: {CONTENT_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    main()
