# Ruazzm

I work on LLM algorithms and systems, especially the parts where model behavior meets infrastructure: post-training, reasoning-time compute, retrieval, agent traces, and serving efficiency.

I prefer small, inspectable projects over broad demos. Good artifacts should leave enough evidence to debug later: configs, traces, metrics, failure cases, and notes about what did not work.

## Current Work

- **Reasoning and post-training:** inference-time compute, verifier signals, preference optimization, RLVR, and reward hacking.
- **Agents and tools:** planning loops, tool-call traces, recovery policies, MCP-style interfaces, and state visibility.
- **Retrieval and memory:** query routing, graph memory, reranking, attribution quality, and stale-context detection.
- **Inference systems:** long-context cost, KV cache policy, prompt caching, speculative decoding, batching, and MoE routing.
- **Multimodal models:** UI/video understanding, mixed-context failures, data curation, and evaluation probes.

## Operating Style

- Reproduce the smallest meaningful claim before scaling it.
- Treat failure cases as first-class data, not appendix material.
- Measure latency, memory, and cost beside quality.
- Keep prompts, configs, seeds, traces, and eval slices visible.
- Prefer boring, repeatable experiments to polished one-off demos.

## Repository Map

| Repo idea | What it should prove |
| --- | --- |
| `reasoning-eval-lab` | Compare direct answering, thinking budgets, self-consistency, verifier reranking, and tool-assisted solving. |
| `agent-trace-bench` | Store agent state, tool calls, retries, and recovery patterns in a format that can be inspected after the run. |
| `rag-failure-atlas` | Taxonomize stale retrieval, citation drift, entity collision, missing context, and multi-hop failure modes. |
| `kv-cache-playground` | Benchmark long-context latency and memory under prompt caching, cache quantization, and compression policies. |
| `posttraining-field-notes` | Keep short implementation notes on SFT, preference optimization, RLVR, rejection sampling, and reward hacking. |

<details>
<summary><strong>Reading queue</strong> - recent signals I use to keep the map from going stale</summary>

<!-- FRONTIER-RADAR:START -->
_Updated on 2026-06-01 UTC. Recent arXiv signals are filtered for LLM relevance; reference anchors fill gaps when a topic is rate-limited._

| Track | Signals |
| --- | --- |
| Reasoning / RLVR | [DeepSeek-R1: reasoning via reinforcement learning](https://arxiv.org/abs/2501.12948)<br>[s1: simple test-time scaling](https://arxiv.org/abs/2501.19393)<br>[Qwen3: hybrid thinking modes](https://qwenlm.github.io/blog/qwen3/) |
| Agents / tool use | [Anthropic Claude 4: extended thinking and tool use](https://www.anthropic.com/news/claude-4)<br>[Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) |
| RAG / memory | [Microsoft GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)<br>[Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) |
| Inference / serving | [Speculative decoding](https://arxiv.org/abs/2211.17192)<br>[vLLM paged attention](https://arxiv.org/abs/2309.06180) |
| Multimodal models | [Qwen3: hybrid thinking modes](https://qwenlm.github.io/blog/qwen3/)<br>[Llama 4: native multimodal MoE models](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)<br>[Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro) |
<!-- FRONTIER-RADAR:END -->

</details>

## Reading Filter

I keep a paper, model release, or engineering note only if it changes at least one implementation choice: the training recipe, inference-time algorithm, tool interface, evaluation method, serving cost model, or failure analysis.
