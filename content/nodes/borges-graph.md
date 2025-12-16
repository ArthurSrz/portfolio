---
title: "Le Graphe de Borges"
type: "nodes"
id: "borges-graph"
shape: "diamond"
parent: "prototypes"
subtitle: "2024 | application"
connectionType: "solid"
weight: 20
draft: false
connections:
  - target: "tech-neo4j"
    label: "BUILT_WITH"
  - target: "tech-nextjs"
    label: "BUILT_WITH"
  - target: "tech-typescript"
    label: "BUILT_WITH"
  - target: "skill-knowledge-graphs"
    label: "REQUIRES"
  - target: "theme-interpretability"
    label: "EXPLORES"
---

# End-to-End GraphRAG for Interpretability Outside the LLM's Mind

Named after Jorge Luis Borges' *"The Library of Babel"* — a universe in the form of a vast library containing all possible books.

[Live Demo](https://le-graphe-de-borges.vercel.app/) | [GitHub](https://github.com/ArthurSrz/borges_graph)

## The Problem with RAG

Traditional RAG systems are black boxes: you ask a question, get an answer, but have no way to understand *how* the LLM arrived at that answer. The reasoning happens inside the model's mind, invisible to users.

## The Solution: GraphRAG with Full Interpretability

Le Graphe de Borges is an **end-to-end GraphRAG implementation** that externalizes the LLM's reasoning into a visible, navigable knowledge graph. Every answer can be traced back through:

1. **Entities** extracted from source texts
2. **Relationships** between entities (who, what, where, when)
3. **Source chunks** - the exact text passages that generated each entity
4. **Community structures** - how entities cluster into themes

## Interpretability Outside the LLM's Mind

Instead of trusting a black-box answer, users can:
- **See the graph** of entities the LLM used to answer
- **Click any node** to view the source text chunk
- **Trace the reasoning path** from question → entities → relationships → answer
- **Verify factual grounding** by reading original passages

This moves interpretability from *inside* the model to *outside* - into a visual, explorable structure that humans can audit and understand.

## Architecture

**Knowledge Graph (Neo4j)**
- 35,000+ entity nodes with semantic relationships
- Community detection for thematic clustering
- Chunk-to-entity provenance tracking

**GraphRAG Pipeline**
- Entity extraction with relationship mapping
- Hybrid search: graph traversal + vector similarity
- Context-aware query enhancement

**3D Visualization (Next.js + Three.js)**
- Force-directed graph with 1000+ visible nodes
- Progressive loading for performance
- Click-through to source text

**Stack**: Neo4j, Next.js, React, TypeScript, Three.js, GraphRAG, Railway, Vercel
