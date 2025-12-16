---
title: "Claude ACE"
type: "nodes"
id: "claude-ace"
shape: "diamond"
parent: "prototypes"
subtitle: "2025-present | in progress | application"
connectionLabel: "Veltys"
connectionType: "solid"
weight: 10
draft: false
connections:
  - target: "theme-interpretability"
    label: "EXPLORES"
  - target: "skill-agent-development"
    label: "USES"
---

# Claude ACE - Agentic Context Engineering

Self-improving Claude agent that learns from interactions using the ACE methodology.

<div class="container">
  <div class="center">
    <button style="color: #778ee7;" onclick="window.open('https://github.com/ArthurSrz/claude-ace', '_blank');">View on GitHub</button>
  </div>
</div>

## Design rationale

Based on the paper ["Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"](https://arxiv.org/abs/2510.04618), this project implements a Claude agent that:

1. **Learns contextually** via an evolving Playbook system
2. **Uses 3 collaborative roles**: Generator, Reflector, Curator
3. **Tracks everything** with Comet ML observability
4. **Persists learnings** between sessions

### ACE Workflow

```
Question → Generator (+ Playbook) → Response
              ↓
Environment → Reflector → Analysis
              ↓
         Curator → Update Playbook
```

## Why This Matters for Interpretability

The ACE architecture makes the agent's learning process **transparent and observable**:
- Each adaptation is logged and visualized
- The Playbook evolution shows what strategies work
- Reflector analyses explain *why* the agent improved

## Technical Stack

- **Claude Agent SDK** - Core agent infrastructure
- **Python** - Implementation language
- **Comet ML** - Observability and tracking
- **Custom Tools** - Playbook manipulation

## Relevance to Anthropic

This project demonstrates hands-on experience with:
- Claude Agent SDK architecture
- Self-improving agent systems
- Observable AI systems design
- Research paper implementation (ACE methodology)
