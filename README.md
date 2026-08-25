# Ruazzm

LLM systems, post-training, and agent evaluation. I spend most of my time around the boundary where model behavior becomes an engineering system: data pipelines, tool interfaces, retrieval, evals, and serving cost models.

I prefer artifacts that can be rerun and inspected. A good AI repo should leave evidence: configs, prompts, traces, tests, eval slices, latency numbers, failure cases, and notes about what did not work.

## Current Public Work

| Surface | Recent evidence | What it signals |
| --- | --- | --- |
| Upstream LLaMA-Factory patches | [Qwen3.5/3.6 tool prompt order](https://github.com/hiyouga/LLaMA-Factory/pull/10534)<br>[multimodal collator batch index](https://github.com/hiyouga/LLaMA-Factory/pull/10535)<br>[Ascend NPU docs link](https://github.com/hiyouga/LLaMA-Factory/pull/10537)<br>[GLM4V video metadata](https://github.com/hiyouga/LLaMA-Factory/pull/10538) | Post-training infrastructure work where tokenizer templates, multimodal data paths, docs, and tests have to line up. |
| Profile knowledge base | [`TECHNICAL_READING_MAP.md`](docs/TECHNICAL_READING_MAP.md)<br>[`FRONTIER_SOURCES.md`](docs/FRONTIER_SOURCES.md)<br>[weekday radar workflow](.github/workflows/update-frontier-radar.yml) | A maintained reading map for papers, docs, and repos that change implementation choices rather than just model names. |

## Workbench

| Track | Questions I care about | Evidence I want in the repo |
| --- | --- | --- |
| Post-training | When does a reward or preference signal change behavior rather than format? | policy deltas, rejected samples, reward hacking cases, ablations |
| Reasoning and evals | When does extra thinking improve accuracy rather than verbosity? | task slices, self-consistency curves, verifier reranking, failure taxonomy |
| Agents and tools | Can an agent explain what it tried, why it retried, and where it lost state? | tool-call traces, state snapshots, recovery logs, replayable runs |
| RAG and memory | Is the answer grounded, or just confidently adjacent to retrieved text? | attribution checks, stale-context tests, entity collisions, reranker comparisons |
| Inference systems | What quality is bought by each extra token, cache entry, and batch slot? | latency/memory dashboards, cache hit rates, batching and quantization notes |
| Multimodal systems | Where do UI, video, and document models confuse space, time, or instruction scope? | frame-level failures, OCR/table probes, data-cleaning notes |

## Operating Loop

```mermaid
flowchart LR
    Claim[Read the claim] --> Repro[Reproduce the smallest useful version]
    Repro --> Instrument[Instrument the run]
    Instrument --> Stress[Attack edge cases]
    Stress --> Write[Write down failures]
    Write --> Ship[Ship a compact artifact]
    Ship --> Claim
```

## Research Shelf

The full map lives in [`docs/TECHNICAL_READING_MAP.md`](docs/TECHNICAL_READING_MAP.md). I keep papers and docs only when they change how I would build, measure, or debug a system.

| Track | Paper anchors | Implementation anchors |
| --- | --- | --- |
| Post-training | [InstructGPT](https://arxiv.org/abs/2203.02155)<br>[DPO](https://arxiv.org/abs/2305.18290)<br>[DeepSeek-R1](https://arxiv.org/abs/2501.12948) | [TRL](https://huggingface.co/docs/trl)<br>[PEFT](https://huggingface.co/docs/peft)<br>[LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) |
| Reasoning / eval | [Self-consistency](https://arxiv.org/abs/2203.11171)<br>[s1](https://arxiv.org/abs/2501.19393)<br>[SWE-bench](https://arxiv.org/abs/2310.06770) | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)<br>[Inspect](https://inspect.aisi.org.uk/)<br>[OpenAI Evals](https://github.com/openai/evals) |
| Agents / tools | [ReAct](https://arxiv.org/abs/2210.03629)<br>[Toolformer](https://arxiv.org/abs/2302.04761)<br>[SWE-agent](https://arxiv.org/abs/2405.15793) | [MCP](https://modelcontextprotocol.io/docs/getting-started/intro)<br>[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)<br>[AutoGen](https://microsoft.github.io/autogen/) |
| RAG / memory | [RAG](https://arxiv.org/abs/2005.11401)<br>[Self-RAG](https://arxiv.org/abs/2310.11511)<br>[RAGAS](https://arxiv.org/abs/2309.15217) | [LlamaIndex](https://docs.llamaindex.ai/)<br>[Haystack evaluation](https://docs.haystack.deepset.ai/docs/evaluation)<br>[Ragas](https://docs.ragas.io/) |
| Inference | [PagedAttention](https://arxiv.org/abs/2309.06180)<br>[Speculative decoding](https://arxiv.org/abs/2211.17192)<br>[FlashAttention](https://arxiv.org/abs/2205.14135) | [vLLM](https://docs.vllm.ai/)<br>[SGLang](https://docs.sglang.io/)<br>[TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/) |
| Data / multimodal | [Self-Instruct](https://arxiv.org/abs/2212.10560)<br>[LLaVA](https://arxiv.org/abs/2304.08485)<br>[MMMU](https://arxiv.org/abs/2311.16502) | [Datasets](https://huggingface.co/docs/datasets)<br>[Datatrove](https://github.com/huggingface/datatrove)<br>[lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) |

## Publish Standard

When I publish an experiment, I want it to include:

- exact model, checkpoint, decoding config, and tool schema,
- data construction notes or the eval slice being used,
- prompts, scoring code, and enough raw traces to inspect mistakes,
- at least one ablation that changes the conclusion if it fails,
- latency, memory, or cost notes when the result depends on serving behavior,
- and a short section on where the result probably does not generalize.

<details>
<summary><strong>Planned artifacts</strong> - repos I want to make inspectable</summary>

| Artifact | Why it should exist |
| --- | --- |
| `reasoning-eval-lab` | Compare direct answering, thinking budgets, self-consistency, verifier reranking, and tool-assisted solving on the same slices. |
| `agent-trace-bench` | Store agent state, tool calls, retries, recovery attempts, and final failure causes in a replayable format. |
| `rag-failure-atlas` | Separate stale retrieval, citation drift, entity collision, missing context, and multi-hop failures instead of calling everything hallucination. |
| `kv-cache-playground` | Measure long-context latency and memory under prompt caching, cache quantization, compression, and batching policies. |
| `posttraining-field-notes` | Keep concise implementation notes on SFT, DPO/IPO/ORPO, RLVR, rejection sampling, reward modeling, and reward hacking. |

</details>

<details>
<summary><strong>Frontier radar</strong> - auto-updated papers and implementation anchors</summary>

<!-- FRONTIER-RADAR:START -->
_Updated on 2026-08-25 UTC. Recent arXiv papers are filtered by track; implementation anchors keep the radar useful when a topic is quiet or rate-limited._

| Track | Recent papers | Implementation anchors |
| --- | --- | --- |
| Post-training / alignment | [How to Train a Critic Stably and Efficiently](http://arxiv.org/abs/2608.23566v1) (2026-08-24)<br>[Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization](http://arxiv.org/abs/2608.23311v1) (2026-08-24) | [TRL docs](https://huggingface.co/docs/trl)<br>[PEFT docs](https://huggingface.co/docs/peft)<br>[LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) |
| Reasoning / evaluation | [How to Train a Critic Stably and Efficiently](http://arxiv.org/abs/2608.23566v1) (2026-08-24)<br>[Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](http://arxiv.org/abs/2608.23497v1) (2026-08-24) | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)<br>[Inspect](https://inspect.aisi.org.uk/)<br>[OpenAI Evals](https://github.com/openai/evals) |
| Agents / tool use | [How Useful are LLMs for Grammar Engineering? Cantonese ParGram Resources and Controlled Experimental Evaluation with English Baselines](http://arxiv.org/abs/2608.23448v1) (2026-08-24)<br>[Automated Construction of FAIR Digital Object Knowledge Graphs from Flat Cultural Heritage Records](http://arxiv.org/abs/2608.23263v1) (2026-08-24) | [MCP docs](https://modelcontextprotocol.io/docs/getting-started/intro)<br>[LangGraph docs](https://docs.langchain.com/oss/python/langgraph/overview)<br>[AutoGen docs](https://microsoft.github.io/autogen/) |
| RAG / memory | [Prime Agent: A Self-Improving RLM Harness](http://arxiv.org/abs/2608.23552v1) (2026-08-24)<br>[When Names Cross Scripts: A Source-Grounded Benchmark for Historical Entity Reconciliation in the Mongol World](http://arxiv.org/abs/2608.23507v1) (2026-08-24) | [LlamaIndex docs](https://docs.llamaindex.ai/)<br>[Haystack evaluation](https://docs.haystack.deepset.ai/docs/evaluation)<br>[Ragas docs](https://docs.ragas.io/)<br>[GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/) |
| Inference / serving | [Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based Person Anomaly Search](http://arxiv.org/abs/2608.23503v1) (2026-08-24)<br>[Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data](http://arxiv.org/abs/2608.23391v1) (2026-08-24) | [vLLM docs](https://docs.vllm.ai/)<br>[SGLang docs](https://docs.sglang.io/)<br>[TensorRT-LLM docs](https://nvidia.github.io/TensorRT-LLM/)<br>[llama.cpp](https://github.com/ggml-org/llama.cpp) |
| Multimodal / documents | [What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](http://arxiv.org/abs/2608.23474v1) (2026-08-24)<br>[CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](http://arxiv.org/abs/2608.23172v1) (2026-08-24) | [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)<br>[VLMEvalKit](https://github.com/open-compass/VLMEvalKit)<br>[LlamaIndex document parsing](https://docs.cloud.llamaindex.ai/) |
| Data / distillation | [Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](http://arxiv.org/abs/2608.23497v1) (2026-08-24)<br>[Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data](http://arxiv.org/abs/2608.23391v1) (2026-08-24) | [Hugging Face Datasets](https://huggingface.co/docs/datasets)<br>[Argilla docs](https://docs.argilla.io/)<br>[Datatrove](https://github.com/huggingface/datatrove) |
<!-- FRONTIER-RADAR:END -->

</details>
