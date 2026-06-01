# GitHub Profile Homepage Implementation

## What to create

Create a public repository named exactly:

```text
Ruazzm
```

GitHub renders `README.md` from `Ruazzm/Ruazzm` at the top of the `github.com/Ruazzm` profile page.

## Files to add

```text
README.md
scripts/update_frontier_radar.py
.github/workflows/update-frontier-radar.yml
docs/FRONTIER_SOURCES.md
docs/TECHNICAL_READING_MAP.md
docs/PROFILE_REVIEW.md
```

After the files are pushed, go to the repository's **Actions** tab and run **Update Frontier Radar** once if you want an immediate refresh. The workflow also runs on weekdays.

## Profile design

The first screen should read like a technical notebook, not a landing page. Keep it calm:

- one clear positioning sentence,
- one compact public-work signal,
- one compact workbench map,
- one operating style section,
- one research shelf,
- and collapsible sections for planned artifacts and the frontier radar.

The reading queue is useful, but it should not dominate the profile. The main page should communicate judgment, current work, and public evidence before automation.

## How to make it look technically deep

Pin repositories that expose real technical work:

- an eval harness with failure cases,
- a small post-training or preference-optimization experiment,
- an agent trace benchmark,
- a RAG failure atlas,
- an inference/cost measurement repo,
- and one clean notes repo that tracks frontier papers with implementation commentary.

Avoid profile clutter that ages badly:

- huge badge walls,
- generic GitHub stats cards,
- "I know Python/React/SQL" technology piles,
- vague AI slogans,
- and old-era claims like prompt engineering as the center of the page.

Prefer current evidence:

- upstream pull requests,
- small regression tests,
- maintained docs,
- repeatable update scripts,
- and links to technical notes that explain why a reference matters.

Use language that can survive model-release cycles:

- say "reasoning-time compute" instead of hyping a single model;
- say "retrieval reliability" instead of only "RAG";
- say "traceable agent systems" instead of "AI agents";
- say "serving cost model" instead of only "deployment";
- say "failure analysis" instead of "benchmarks" when the artifact includes real cases.

## Recommended first repo backlog

1. `reasoning-eval-lab`
   Compare direct answer, thinking mode, self-consistency, verifier reranking, and tool-assisted solving.

2. `rag-failure-atlas`
   Taxonomize hallucination, stale retrieval, citation drift, entity collision, and multi-hop retrieval failures.

3. `agent-trace-bench`
   Store tool-call traces, task state, retries, and recovery patterns for coding or browser agents.

4. `kv-cache-playground`
   Benchmark long-context latency, memory, cache quantization, and prompt caching.

5. `llm-posttraining-notes`
   Short implementation notes for SFT, DPO, IPO, ORPO, RLVR, rejection sampling, reward modeling, and reward hacking.

## Frontiers this profile is tuned for

- reasoning models with explicit thinking budgets,
- reinforcement learning with verifiable rewards,
- hybrid thinking/non-thinking modes,
- long-context and native multimodality,
- MoE serving economics,
- agentic tool use,
- MCP-style tool ecosystems,
- retrieval as an attribution system,
- and inference-time scaling rather than only pretraining scale.
