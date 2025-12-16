---
title: "RAG Design"
type: "nodes"
id: "rag-design"
shape: "diamond"
parent: "prototypes"
subtitle: "2025-present | in progress | research"
connectionLabel: "Side-project"
connectionType: "solid"
weight: 25
draft: false
connections:
  - target: "tech-langchain"
    label: "BUILT_WITH"
  - target: "theme-interpretability"
    label: "EXPLORES"
---

# RAG Design

Experimental notebooks testing different RAG (Retrieval-Augmented Generation) architectures with local models.

<div class="container">
  <div class="center">
    <button style="color: #778ee7;" onclick="window.open('https://github.com/ArthurSrz/RAGdesign', '_blank');">View on GitHub</button>
  </div>
</div>

## Design rationale

RAG systems are increasingly central to practical LLM applications, but their design space is vast. This project provides a controlled environment to test different:

- **Chunking strategies** - How to split documents
- **Embedding models** - Which representations work best
- **Retrieval methods** - Similarity search vs hybrid approaches
- **Generation patterns** - How to condition the LLM

## Components

### 1. Data Ingestion (`ingestion.ipynb`)
- Document parsing and preprocessing
- Chunking strategy experiments
- Embedding generation with local models

### 2. Retrieval & Generation (`retrieval_generation.ipynb`)
- Vector similarity search
- Re-ranking experiments
- LLM generation with retrieved context

## Why Local Models?

Running models locally enables:
- **Full observability** of intermediate states
- **Reproducible experiments** without API variability
- **Cost-effective iteration** for research purposes

## Technical Stack

- Python
- Local embedding models
- Vector stores
- Open-source LLMs
