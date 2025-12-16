---
title: "Intuitiveness"
type: "nodes"
id: "intuitiveness"
shape: "diamond"
parent: "prototypes"
subtitle: "2023-present | research"
connectionType: "solid"
weight: 12
draft: false
connections:
  - target: "theme-interpretability"
    label: "EXPLORES"
  - target: "theme-hdi"
    label: "EXPLORES"
  - target: "datactivist"
    label: "BUILT_FOR"
  - target: "tech-neo4j"
    label: "BUILT_WITH"
  - target: "tech-python"
    label: "BUILT_WITH"
  - target: "skill-design-science"
    label: "REQUIRES"
  - target: "data-redesign-method"
    label: "IMPLEMENTS"
  - target: "design-science-researcher"
    label: "BUILT_DURING"
---

# Intuitiveness: Decreasing System Complexity through Data Redesign

[![DOI](https://zenodo.org/badge/685140191.svg)](https://zenodo.org/badge/latestdoi/685140191)

A methodology for transforming raw, complex datasets into purpose-built data that directly answers your questions.

[GitHub](https://github.com/ArthurSrz/intuitiveness) | [Scientific Paper](https://github.com/ArthurSrz/intuitiveness/blob/main/scientific_article/Intuitiveness.pdf)

## The Descent-Ascent Methodology

The method reduces complexity through a **descent-ascent cycle**:
- **Descent** (L4 → L0): Strip away complexity to find the core truth
- **Ascent** (L0 → L3): Rebuild with YOUR intent, adding only relevant dimensions

### The 5 Levels of Abstraction

| Level | Name | Description |
|-------|------|-------------|
| **L4** | Raw Dataset | Original tabular data |
| **L3** | Entity Graph | Knowledge graph of relationships |
| **L2** | Domain Categories | Grouped by semantic domains |
| **L1** | Feature Vector | Unified numeric representation |
| **L0** | Core Datum | Single atomic value (the truth) |

## Key Features

- **Natural Language Search**: Query French open data in plain French using SmolLM3-3B
- **Knowledge Graph**: Neo4j-powered entity relationships for interpretability
- **Semantic Matching**: AI-assisted domain categorization
- **Interactive Workflow**: Visual descent-ascent in Streamlit

## Research Context

Part of the [Dataflow](https://dataflow.hypotheses.org/) research project, exploring how to make data systems interpretable by design.

**Stack**: Python, Neo4j, Streamlit, SmolLM3-3B, HuggingFace