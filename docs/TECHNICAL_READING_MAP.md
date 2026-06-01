# Technical Reading Map

This is the longer reading map behind the profile README. It is intentionally biased toward papers, docs, and repos that change how an experiment is built, measured, or debugged.

## How I Use This Map

| Rule | Why it matters |
| --- | --- |
| Keep implementation anchors beside papers. | A paper changes the direction; docs reveal the engineering surface area. |
| Prefer evals with inspectable errors. | Metrics are only useful when the failure slice is easy to replay. |
| Track serving and data work as first-class research. | Many model-quality claims disappear when latency, memory, or data construction changes. |
| Avoid model-release sprawl. | A release note belongs here only if it changes the training recipe, inference path, eval method, or tool interface. |

## Post-Training And Alignment

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | paper | SFT plus reward modeling plus PPO as a practical alignment pipeline. |
| [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | paper | Preference optimization without an explicit reward model loop. |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | paper | RL signal design for reasoning behavior and long-CoT distillation. |
| [TRL](https://huggingface.co/docs/trl) | docs | SFT, reward modeling, DPO, GRPO, online methods, and trainer APIs. |
| [PEFT](https://huggingface.co/docs/peft) | docs | LoRA/adapter mechanics, merge behavior, and fine-tuning cost control. |
| [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) | repo/docs | End-to-end supervised fine-tuning, preference optimization, and deployment recipes. |

## Reasoning And Evaluation

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) | paper | Sampling and aggregation as a simple inference-time reasoning lever. |
| [s1: simple test-time scaling](https://arxiv.org/abs/2501.19393) | paper | Budgeted thinking as an algorithmic variable rather than a vague behavior. |
| [SWE-bench](https://arxiv.org/abs/2310.06770) | paper/benchmark | Real software tasks, patch validation, and benchmark leakage risks. |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | repo/docs | Reproducible task configs, backend adapters, and prompt-level comparability. |
| [Inspect](https://inspect.aisi.org.uk/) | docs | Eval scaffolding, task solvers, scorers, logging, and reproducible runs. |
| [OpenAI Evals](https://github.com/openai/evals) | repo | Dataset/scorer structure and repeatable eval packaging. |

## Agents And Tool Use

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [ReAct](https://arxiv.org/abs/2210.03629) | paper | Interleaving reasoning and acting, plus traces as debugging artifacts. |
| [Toolformer](https://arxiv.org/abs/2302.04761) | paper | Tool-use data construction and self-supervised API-call learning. |
| [SWE-agent](https://arxiv.org/abs/2405.15793) | paper/repo | Agent-computer interface design for real coding tasks. |
| [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) | docs | Tool and data-source boundaries that can survive across clients. |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | docs | Durable agent state, graph execution, interrupts, and replayable workflows. |
| [AutoGen](https://microsoft.github.io/autogen/) | docs | Multi-agent orchestration, tool execution, and conversation patterns. |

## RAG, Memory, And Attribution

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) | paper | Parametric versus non-parametric memory as a system design split. |
| [Self-RAG](https://arxiv.org/abs/2310.11511) | paper | Retrieval decisions, critique tokens, and attribution-aware generation. |
| [RAGAS](https://arxiv.org/abs/2309.15217) | paper | Reference-free RAG evaluation dimensions and their limits. |
| [LlamaIndex](https://docs.llamaindex.ai/) | docs | Ingestion, indexing, retrieval, query engines, agents, and eval integrations. |
| [Haystack evaluation](https://docs.haystack.deepset.ai/docs/evaluation) | docs | Component-level versus end-to-end RAG evaluation patterns. |
| [Ragas](https://docs.ragas.io/) | docs | RAG metrics, explainability notes, and trace inspection. |
| [GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/) | docs/project | Graph-structured retrieval and entity/community summarization patterns. |

## Inference And Serving Systems

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180) | paper | KV-cache paging as a serving architecture primitive. |
| [Speculative decoding](https://arxiv.org/abs/2211.17192) | paper | Draft/verify decoding and the quality-latency trade. |
| [FlashAttention](https://arxiv.org/abs/2205.14135) | paper | Memory-aware attention kernels and IO-bound performance thinking. |
| [vLLM](https://docs.vllm.ai/) | docs | OpenAI-compatible serving, continuous batching, prefix caching, quantization, distributed inference. |
| [SGLang](https://docs.sglang.io/) | docs | Structured generation, radix cache, serving benchmarks, and multimodal serving. |
| [TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/) | docs | NVIDIA inference stack, quantization, batching, and deployment surfaces. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | repo/docs | Local inference, quantization formats, CPU/GPU portability, and edge deployment. |

## Multimodal And Document Understanding

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [LLaVA](https://arxiv.org/abs/2304.08485) | paper | Visual instruction tuning and data generation strategy. |
| [MMMU](https://arxiv.org/abs/2311.16502) | paper/benchmark | Multidiscipline multimodal reasoning eval design. |
| [DocVQA](https://arxiv.org/abs/2007.00398) | paper/benchmark | Document QA as a grounded visual-language task. |
| [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | repo | Multimodal benchmark runner and task adapters. |
| [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | repo | Vision-language model evaluation and leaderboard-style comparisons. |
| [LlamaCloud parsing](https://docs.cloud.llamaindex.ai/) | docs | Document parsing, structured extraction, and retrieval-oriented ingestion. |

## Data, Distillation, And Curation

| Resource | Type | What I extract from it |
| --- | --- | --- |
| [Self-Instruct](https://arxiv.org/abs/2212.10560) | paper | Bootstrapping instruction data and filtering synthetic samples. |
| [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) | project note | Low-cost instruction-following data recipe and reproducibility caveats. |
| [Magpie](https://arxiv.org/abs/2406.08464) | paper | Self-synthesis of instruction data from aligned models. |
| [Hugging Face Datasets](https://huggingface.co/docs/datasets) | docs | Dataset loading, streaming, processing, and reproducible dataset cards. |
| [Argilla](https://docs.argilla.io/) | docs | Human feedback workflows and data annotation surfaces. |
| [Datatrove](https://github.com/huggingface/datatrove) | repo | Large-scale text processing, filtering, deduplication, and dataset pipelines. |

## Auto-Update Policy

The profile README has a GitHub Actions job that refreshes the frontier radar on weekdays. The dynamic radar should stay small enough to scan, while this file stays as the slower-moving reference shelf.
