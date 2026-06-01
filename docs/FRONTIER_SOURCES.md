# Frontier Source Notes

These are the slower-moving source anchors behind the README radar. The automated section in the profile reads fresh arXiv submissions, then falls back to these kinds of references when a track is quiet or rate-limited.

## Radar Tracks

| Track | What counts as signal | Stable anchors |
| --- | --- | --- |
| Post-training / alignment | Reward modeling, preference optimization, RLVR, GRPO/DPO variants, reward hacking, distillation | [TRL](https://huggingface.co/docs/trl), [PEFT](https://huggingface.co/docs/peft), [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) |
| Reasoning / evaluation | Test-time compute, verifier reranking, eval harness design, benchmark leakage, coding-agent tasks | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), [Inspect](https://inspect.aisi.org.uk/), [OpenAI Evals](https://github.com/openai/evals) |
| Agents / tool use | Tool-call interfaces, agent state, planning loops, browser/computer use, recovery policy | [MCP](https://modelcontextprotocol.io/docs/getting-started/intro), [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), [AutoGen](https://microsoft.github.io/autogen/) |
| RAG / memory | Retrieval evaluation, attribution, reranking, stale context, GraphRAG, long-context failure cases | [LlamaIndex](https://docs.llamaindex.ai/), [Haystack evaluation](https://docs.haystack.deepset.ai/docs/evaluation), [Ragas](https://docs.ragas.io/), [GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/) |
| Inference / serving | KV cache policy, speculative decoding, prefix caching, batching, quantization, latency/throughput | [vLLM](https://docs.vllm.ai/), [SGLang](https://docs.sglang.io/), [TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/), [llama.cpp](https://github.com/ggml-org/llama.cpp) |
| Multimodal / documents | VLM evals, document QA, UI/video understanding, OCR failures, chart/table grounding | [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval), [VLMEvalKit](https://github.com/open-compass/VLMEvalKit), [LlamaCloud parsing](https://docs.cloud.llamaindex.ai/) |
| Data / distillation | Synthetic data, data filtering, instruction tuning, distillation, preference data collection | [Hugging Face Datasets](https://huggingface.co/docs/datasets), [Argilla](https://docs.argilla.io/), [Datatrove](https://github.com/huggingface/datatrove) |

## Keep / Drop Filter

Keep a paper, release note, or doc page only if it changes at least one of these:

- the training or post-training recipe,
- the inference-time algorithm,
- the tool or agent interface,
- the evaluation method,
- the serving cost model,
- the data construction pipeline,
- or the failure analysis.

Drop pure model leaderboard announcements unless they expose a reusable training recipe, eval design, serving technique, or dataset construction detail.
