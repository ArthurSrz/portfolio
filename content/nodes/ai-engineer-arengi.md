---
title: "AI Engineer"
type: "nodes"
id: "ai-engineer-arengi"
shape: "square"
parent: "experiences"
subtitle: "2024-present"
connectionType: "solid"
weight: 20
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

Put a Large Language Model in production for Arengi (via Veltys mission), covering the complete stack from GPU optimization to alignment.

## GPU Optimization

Configured and optimized a 4x Tesla V100S GPU cluster (32GB VRAM each) for maximum inference throughput:

- **Tensor Parallelism**: Distributed Mixtral 8x7B (170GB) across 4 GPUs using vLLM's tensor-parallel-size=4
- **Memory Optimization**: Set `gpu-memory-utilization=0.98` and `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- **Quantization**: Tested GPTQ quantized models (Llama-2-70B-Chat-GPTQ) for memory-constrained scenarios
- **CPU Offloading**: Configured `cpu-offload-gb=140` and `swap-space=20` for larger models
- **Chunked Prefill**: Disabled for Meta Llama models to avoid compatibility issues

## Inference Layer (vLLM)

- OpenAI-compatible API server on port 8060
- Support for Mixtral 8x7B, Llama-3.2, Mistral-7B models
- Half-precision (FP16) inference for V100 Compute Capability 7.0

## Orchestration Layer (LangChain)

- RAG pipelines with document retrieval and generation
- Prompt management for insurance domain tasks
- Chain-of-thought observability with Opik

## Vector Database (OpenSearch)

- Document embedding with multilingual-e5-large-instruct
- Semantic search for RAG-enhanced responses

## Alignment & Evaluation

- Streamlit annotation interface for domain expert feedback
- Evaluation datasets and metrics for model performance

**Stack**: vLLM, LangChain, OpenSearch, Opik, FastAPI, Streamlit, CUDA 12.7
