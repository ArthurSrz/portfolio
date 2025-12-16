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

# Interactive 3D Knowledge Graph for Literary Analysis

Named after Jorge Luis Borges' *"The Library of Babel"* — a universe in the form of a vast library containing all possible books.

[Live Demo](https://le-graphe-de-borges.vercel.app/) | [GitHub](https://github.com/ArthurSrz/nano-graphrag)

## What it does

Borges Library lets you explore literary works through their knowledge graphs. Ask questions in natural language, and see how entities (people, places, concepts) connect across different books.

- **Multi-book querying**: Ask questions across your entire library at once
- **3D force-directed graph**: Interactive visualization with color-coded entity types
- **End-to-end interpretability**: Click any entity to see the source text that generated it

## Architecture

The system is composed of two main components:

**Frontend (Next.js 16 + React 19)**
- 3D graph visualization using Three.js and D3.js
- Natural language query interface
- Source text provenance panels

**Backend (Reconciliation API)**
- Coordinates between Neo4j graph database and GraphRAG queries
- Progressive graph loading (300 → 400 → 500 → 1000 nodes)
- Context-aware GraphRAG with visible nodes as context

## Design Principles

1. No orphaned nodes - All displayed entities must have relationships
2. Books at center - Books are core entities, always central to queries
3. Inter-book exploration - Connections between books are prioritized
4. Visual clarity - Space between nodes to see relationships clearly
5. Full interpretability - Navigate from text chunks to RAG answers through the graph

**Stack**: Next.js, React, TypeScript, Three.js, Neo4j, GraphRAG, Railway, Vercel