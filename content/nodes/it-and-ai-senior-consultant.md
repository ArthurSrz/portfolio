---
title: "IT and AI Senior Consultant"
type: "nodes"
id: "it-and-ai-senior-consultant"
shape: "square"
parent: "experiences"
subtitle: "2024-present"
connectionLabel: "Veltys"
connectionType: "solid"
weight: 20
draft: false
connections:
  - target: "veltys"
    label: "AT"
  - target: "slm-in-production"
    label: "BUILT"
  - target: "theme-interpretability"
    label: "EXPLORES"
---

As an IT & AI Senior Consultant at Veltys, I bridge the gap between non-technical clients and engineers developing AI systems.

## Production LLM Deployment

Put a Large Language Model in production for an insurance client, covering the complete stack from GPU optimization to alignment.

### GPU Optimization

Configured and optimized a 4x Tesla V100S GPU cluster (32GB VRAM each) for maximum inference throughput:

- **Tensor Parallelism**: Distributed Mixtral 8x7B (170GB) across 4 GPUs using vLLM's tensor-parallel-size=4
- **Memory Optimization**: Set `gpu-memory-utilization=0.98` and `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- **Quantization**: Tested GPTQ quantized models (Llama-2-70B-Chat-GPTQ) for memory-constrained scenarios
- **CPU Offloading**: Configured `cpu-offload-gb=140` and `swap-space=20` for larger models

### Inference Layer (vLLM)

- OpenAI-compatible API server
- Support for Mixtral 8x7B, Llama-3.2, Mistral-7B models
- Half-precision (FP16) inference for V100 Compute Capability 7.0

### Orchestration & Observability

- LangChain RAG pipelines with prompt management
- Opik for chain-of-thought tracing and evaluation
- OpenSearch vector database with multilingual-e5-large embeddings

### Alignment & Evaluation

- Streamlit annotation interface for domain expert feedback
- Custom evaluation datasets and metrics

## Knowledge Graph Systems

Design interpretable knowledge graphs for deep tech start-ups, acting both as semantic layers for IT systems and as IP assets to increase valuation.

**Stack**: vLLM, LangChain, OpenSearch, Opik, FastAPI, Streamlit, Neo4j, CUDA 12.7
