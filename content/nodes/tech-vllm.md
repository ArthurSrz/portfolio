---
title: "vLLM"
type: "nodes"
id: "tech-vllm"
shape: "triangle"
parent: "technologies"
subtitle: "LLM Inference"
connectionType: "solid"
weight: 12
draft: false
---

vLLM is a high-throughput, memory-efficient inference engine for Large Language Models. It uses PagedAttention to manage GPU memory efficiently, enabling serving of large models with optimal throughput.

Key features used:
- Tensor parallelism for multi-GPU serving
- OpenAI-compatible API
- Continuous batching
- GPTQ quantization support
