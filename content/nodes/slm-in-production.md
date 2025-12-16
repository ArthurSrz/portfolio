---
title: "SLM in Production"
type: "nodes"
id: "slm-in-production"
shape: "diamond"
parent: "prototypes"
subtitle: "2024 | application"
connectionType: "solid"
weight: 22
draft: false
connections:
  - target: "tech-vllm"
    label: "INFERENCE"
  - target: "tech-langchain"
    label: "ORCHESTRATION"
  - target: "tech-opik"
    label: "OBSERVABILITY"
  - target: "tech-python"
    label: "BUILT_WITH"
  - target: "skill-llm-evaluation"
    label: "REQUIRES"
  - target: "theme-interpretability"
    label: "EXPLORES"
  - target: "it-and-ai-senior-consultant"
    label: "BUILT_DURING"
---

# Sovereign LLM Deployment

End-to-end deployment of a Small Language Model in production for an insurance client, from GPU cluster configuration to model alignment.

## Architecture

**GPU Cluster**: 4x Tesla V100S (32GB VRAM each)
- Tensor parallelism across 4 GPUs
- Memory utilization at 98%
- CPU offloading for larger models

**Inference (vLLM)**
- OpenAI-compatible API
- Mixtral 8x7B, Llama-3.2, Mistral-7B
- Half-precision (FP16) for V100

**Orchestration (LangChain)**
- RAG pipelines with OpenSearch
- Prompt management
- Chain-of-thought logging

**Observability (Opik)**
- Trace visualization
- Evaluation metrics
- Experiment tracking

## Alignment

- Streamlit annotation interface
- Domain expert feedback loops
- Custom evaluation datasets

**Stack**: vLLM, LangChain, OpenSearch, Opik, FastAPI, CUDA 12.7
