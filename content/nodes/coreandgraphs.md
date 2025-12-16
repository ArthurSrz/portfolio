---
title: "Core & Graphs"
subtitle: "2025-present | in progress | framework"
shape: "diamond"
parent: "prototypes"
connections:
  - target: "tech-neo4j"
    label: "USES_TECHNOLOGY"
  - target: "skill-knowledge-graphs"
    label: "DEMONSTRATES_SKILL"
  - target: "theme-hdi"
    label: "EXPLORES_THEME"
---

# Core & Graphs

A new approach to data governance through collaborative knowledge graphs.

<div class="container">
  <div class="center">
    <button style="color: #778ee7;" onclick="window.open('https://arthursrz.github.io/documente-marcel/', '_blank');">Documentation</button>
  </div>
</div>

## Design rationale

Traditional data governance is document-heavy and disconnected from actual data flows. Core & Graphs reimagines governance as **living knowledge graphs** that evolve with the organization.

## Sub-projects

### graphandgovern
Core governance framework - connecting data policies to actual data assets through graph relationships.

### graphandvisualize
A collaborative knowledge graph for data visualization best practices. Helps analysts identify conceptual forces between ideas and represent them visually.

### graphandopenmodels
Governance patterns for open models and open data integration.

## Philosophy

> "Une nouvelle manière de gouverner les données."

Governance should be:
- **Visual** - graphs make relationships clear
- **Collaborative** - multiple contributors enrich the model
- **Living** - the graph evolves with the organization

## Technical Stack

- Neo4j for graph storage
- MCP servers for Claude integration
- [documente-marcel](https://arthursrz.github.io/documente-marcel/) for documentation
