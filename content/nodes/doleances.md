---
title: "Doléances"
type: "nodes"
id: "doleances"
shape: "diamond"
parent: "prototypes"
subtitle: "2025-present | done | research"
connectionLabel: "Heretica"
connectionType: "solid"
weight: 10
draft: false
connections:
  - target: "tech-pytorch"
    label: "BUILT_WITH"
  - target: "theme-open-data"
    label: "EXPLORES"
---

# Ce que veulent les Français

Democratic exploitation of the French "Cahiers de Doléances" (grievance notebooks) using LLMs and French-specific NLP.

## Design rationale

The 2019 Grand Débat National generated thousands of grievance notebooks from French citizens. This project makes this democratic corpus **accessible and analyzable** using modern NLP techniques.

## Methodology

### 1. Data Ingestion
- Source: [Transcribed grievances](https://www.marieannechabin.fr/edition-de-cahiers-doleances-2019/)
- Cleaned non-grievance pages to reduce noise
- Preserved authentic citizen voice

### 2. French-First NLP
Using **CamemBERT** - a language model trained exclusively on French text, unlike multilingual models that may miss French linguistic nuances.

Why CamemBERT over multilingual models:
- Trained on 138GB of French text
- Better captures French syntax and semantics
- More accurate embeddings for French civic discourse

### 3. Vectorization & Analysis
- Generated embeddings for semantic clustering
- Identified thematic patterns across grievances
- Enabled semantic search through citizen concerns

## Technical Stack

- Python
- CamemBERT (Hugging Face)
- Vector embeddings
- Statistical analysis

## Democratic Tech

This project embodies a key principle: **technology should serve democratic participation**. By making citizen voices analyzable, we enable:
- Policymakers to understand constituents
- Researchers to study civic discourse
- Citizens to see their concerns in context

## Relevance to Interpretability

The project applies interpretability principles to **democratic discourse**:
- Making implicit citizen concerns explicit
- Clustering to reveal emergent themes
- Semantic search for navigating large corpora
