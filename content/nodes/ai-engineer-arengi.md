---
title: "AI Engineer"
type: "nodes"
id: "ai-engineer-arengi"
shape: "square"
parent: "experiences"
subtitle: "2024-present"
connectionType: "solid"
weight: 15
draft: false
connections:
  - target: "arengi"
    label: "AT"
  - target: "tech-pytorch"
    label: "USES"
  - target: "tech-python"
    label: "USES"
  - target: "skill-agent-development"
    label: "REQUIRES"
  - target: "theme-interpretability"
    label: "EXPLORES"
---

# Production SLM from GPU to Alignment

Led the end-to-end deployment of a sovereign Small Language Model (SLM) in production, covering the complete stack from hardware to alignment:

**Infrastructure Layer**
- Configured and optimized a 4x Tesla V100S GPU cluster
- Set up VLLM serving infrastructure with tensor parallelism
- Implemented FastAPI backend for chat and RAG endpoints

**Model Layer**
- Deployed Mixtral 8x7B and Llama models with optimized inference
- Implemented RAG-enhanced chat with OpenSearch embeddings
- Fine-tuned prompts for insurance domain tasks

**Alignment & Observability**
- Built Streamlit annotation interface for domain expert feedback
- Created evaluation datasets and metrics for model performance
- Established chain-of-thought observability infrastructure

**Stack**: VLLM, FastAPI, Streamlit, OpenSearch, CUDA 12.7
