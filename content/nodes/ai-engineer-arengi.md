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
  - target: "veltys"
    label: "VIA"
  - target: "tech-langchain"
    label: "USES"
  - target: "tech-opik"
    label: "USES"
  - target: "tech-python"
    label: "USES"
  - target: "skill-agent-development"
    label: "REQUIRES"
  - target: "skill-llm-evaluation"
    label: "REQUIRES"
  - target: "theme-interpretability"
    label: "EXPLORES"
---

# Production LLM Deployment

Put a Large Language Model in production for Arengi (via Veltys mission), covering the complete stack:

**Inference Layer (vLLM)**
- Configured 4x Tesla V100S GPU cluster with tensor parallelism
- Optimized vLLM serving for Mixtral 8x7B and Llama models
- FastAPI backend exposing chat and RAG endpoints

**Orchestration Layer (LangChain)**
- Built RAG pipelines with document retrieval and generation
- Implemented prompt management for insurance domain tasks
- Chain-of-thought observability for debugging and monitoring

**Vector Database (OpenSearch)**
- Document embedding with multilingual-e5-large model
- Semantic search for RAG-enhanced responses
- Index management for multiple document collections

**Alignment & Evaluation**
- Streamlit annotation interface for domain expert feedback
- Evaluation datasets and metrics for model performance

**Stack**: vLLM, LangChain, OpenSearch, FastAPI, Streamlit, CUDA 12.7
