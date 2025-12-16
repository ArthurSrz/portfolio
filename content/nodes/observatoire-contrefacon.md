---
title: "Observatoire Contrefaçon"
subtitle: "2025-present | done | application"
shape: "diamond"
parent: "prototypes"
connections:
  - target: "tech-neo4j"
    label: "USES_TECHNOLOGY"
  - target: "skill-knowledge-graphs"
    label: "DEMONSTRATES_SKILL"
---

# Observatoire de la Contrefaçon dans le Luxe

Real-time counterfeit pattern analysis dashboard for the luxury industry, built on a Neo4j knowledge graph.

<div class="container">
  <div class="center">
    <button style="color: #778ee7;" onclick="window.open('https://observatoire-contrefacon.vercel.app', '_blank');">Live Demo</button>
  </div>
</div>

## Design rationale

Based on the **Rapport Colbert 2025**, this application provides:

- Critical route identification for counterfeit goods
- Vulnerable free trade zone detection (inspection rate < 5%)
- Technology-channel correlation analysis
- Emerging threat prediction (AI, Super Fakes AAA+)

## Knowledge Graph Structure

**60 nodes** across 8 types:
- Technologies, Channels, Countries
- Categories, Techniques, Zones
- Actors, Metrics

**75 relationships** modeling complete counterfeit chains

## Key Metrics Tracked

| Metric | Value |
|--------|-------|
| Total seizures 2024 | $11.82B (+45%) |
| Jewelry | $1.65B (30%) |
| Super Fakes detection | 2% |
| Temu growth | +6300% |

## Technical Stack

- **Frontend**: Next.js 15, React 18, TypeScript
- **Visualization**: Recharts, D3.js, Framer Motion
- **Database**: Neo4j (via MCP)
- **Deployment**: Vercel

## Relevance to Interpretability

This project demonstrates how **knowledge graphs make complex systems interpretable**:
- Users can trace counterfeit routes end-to-end
- Threat scores are explainable through graph traversal
- Correlations emerge from graph structure, not black-box ML
