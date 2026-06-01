#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import html
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- FRONTIER-RADAR:START -->"
END = "<!-- FRONTIER-RADAR:END -->"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_DELAY_SECONDS = 3.2
HTTP_TIMEOUT_SECONDS = 35
MAX_RESULTS_PER_TRACK = 6
MAX_PAPERS_PER_TRACK = 2
MAX_RETRIES = 2


TRACKS = [
    {
        "label": "Post-training / alignment",
        "query": 'cat:cs.CL AND (all:"large language model" OR all:"LLM") AND (all:"post-training" OR all:"alignment" OR all:"preference optimization" OR all:"RLHF" OR all:"DPO" OR all:"GRPO" OR all:"reward model")',
        "needles": (
            "alignment",
            "preference",
            "rlhf",
            "dpo",
            "grpo",
            "reward model",
            "post-training",
            "post training",
        ),
        "fallback_papers": [
            ("Training language models to follow instructions with human feedback", "https://arxiv.org/abs/2203.02155"),
            ("Direct Preference Optimization", "https://arxiv.org/abs/2305.18290"),
            ("DeepSeek-R1: reasoning via reinforcement learning", "https://arxiv.org/abs/2501.12948"),
        ],
        "anchors": [
            ("TRL docs", "https://huggingface.co/docs/trl"),
            ("PEFT docs", "https://huggingface.co/docs/peft"),
            ("LLaMA Factory", "https://github.com/hiyouga/LLaMA-Factory"),
        ],
    },
    {
        "label": "Reasoning / evaluation",
        "query": 'cat:cs.CL AND (all:"large language model" OR all:"LLM") AND (all:"reasoning" OR all:"test-time compute" OR all:"verifier" OR all:"evaluation" OR all:"benchmark")',
        "needles": (
            "reasoning",
            "test-time",
            "test time",
            "verifier",
            "benchmark",
            "evaluation",
            "chain-of-thought",
        ),
        "fallback_papers": [
            ("Self-Consistency Improves Chain of Thought Reasoning", "https://arxiv.org/abs/2203.11171"),
            ("s1: simple test-time scaling", "https://arxiv.org/abs/2501.19393"),
            ("SWE-bench", "https://arxiv.org/abs/2310.06770"),
        ],
        "anchors": [
            ("lm-evaluation-harness", "https://github.com/EleutherAI/lm-evaluation-harness"),
            ("Inspect", "https://inspect.aisi.org.uk/"),
            ("OpenAI Evals", "https://github.com/openai/evals"),
        ],
    },
    {
        "label": "Agents / tool use",
        "query": 'cat:cs.CL AND (all:"large language model" OR all:"LLM") AND (all:"agent" OR all:"tool use" OR all:"tool-use" OR all:"computer use" OR all:"workflow")',
        "needles": (
            "agent",
            "tool",
            "computer use",
            "workflow",
            "planning",
            "environment",
            "web",
        ),
        "fallback_papers": [
            ("ReAct: Synergizing Reasoning and Acting", "https://arxiv.org/abs/2210.03629"),
            ("Toolformer", "https://arxiv.org/abs/2302.04761"),
            ("SWE-agent", "https://arxiv.org/abs/2405.15793"),
        ],
        "anchors": [
            ("MCP docs", "https://modelcontextprotocol.io/docs/getting-started/intro"),
            ("LangGraph docs", "https://docs.langchain.com/oss/python/langgraph/overview"),
            ("AutoGen docs", "https://microsoft.github.io/autogen/"),
        ],
    },
    {
        "label": "RAG / memory",
        "query": 'cat:cs.CL AND (all:"retrieval augmented generation" OR all:"RAG" OR all:"GraphRAG" OR all:"reranking" OR all:"grounding" OR all:"long context")',
        "needles": (
            "retrieval",
            "rag",
            "graphrag",
            "rerank",
            "grounding",
            "citation",
            "memory",
            "long-context",
        ),
        "fallback_papers": [
            ("Retrieval-Augmented Generation", "https://arxiv.org/abs/2005.11401"),
            ("Self-RAG", "https://arxiv.org/abs/2310.11511"),
            ("RAGAS", "https://arxiv.org/abs/2309.15217"),
        ],
        "anchors": [
            ("LlamaIndex docs", "https://docs.llamaindex.ai/"),
            ("Haystack evaluation", "https://docs.haystack.deepset.ai/docs/evaluation"),
            ("Ragas docs", "https://docs.ragas.io/"),
            ("GraphRAG", "https://www.microsoft.com/en-us/research/project/graphrag/"),
        ],
    },
    {
        "label": "Inference / serving",
        "query": '(all:"large language model" OR all:"LLM") AND (all:"inference" OR all:"serving" OR all:"KV cache" OR all:"speculative decoding" OR all:"continuous batching" OR all:"prefix caching")',
        "needles": (
            "inference",
            "serving",
            "kv cache",
            "speculative",
            "batching",
            "prefix caching",
            "pagedattention",
            "latency",
            "throughput",
        ),
        "fallback_papers": [
            ("PagedAttention / vLLM", "https://arxiv.org/abs/2309.06180"),
            ("Speculative Decoding", "https://arxiv.org/abs/2211.17192"),
            ("FlashAttention", "https://arxiv.org/abs/2205.14135"),
        ],
        "anchors": [
            ("vLLM docs", "https://docs.vllm.ai/"),
            ("SGLang docs", "https://docs.sglang.io/"),
            ("TensorRT-LLM docs", "https://nvidia.github.io/TensorRT-LLM/"),
            ("llama.cpp", "https://github.com/ggml-org/llama.cpp"),
        ],
    },
    {
        "label": "Multimodal / documents",
        "query": 'cat:cs.CL AND (all:"multimodal" OR all:"vision language model" OR all:"VLM" OR all:"document understanding" OR all:"video understanding" OR all:"UI")',
        "needles": (
            "multimodal",
            "vision-language",
            "vision language",
            "vlm",
            "document",
            "video",
            "ui",
            "chart",
        ),
        "fallback_papers": [
            ("LLaVA", "https://arxiv.org/abs/2304.08485"),
            ("MMMU", "https://arxiv.org/abs/2311.16502"),
            ("DocVQA", "https://arxiv.org/abs/2007.00398"),
        ],
        "anchors": [
            ("lmms-eval", "https://github.com/EvolvingLMMs-Lab/lmms-eval"),
            ("VLMEvalKit", "https://github.com/open-compass/VLMEvalKit"),
            ("LlamaIndex document parsing", "https://docs.cloud.llamaindex.ai/"),
        ],
    },
    {
        "label": "Data / distillation",
        "query": 'cat:cs.CL AND (all:"large language model" OR all:"LLM") AND (all:"synthetic data" OR all:"data curation" OR all:"distillation" OR all:"instruction tuning" OR all:"dataset")',
        "needles": (
            "synthetic data",
            "data curation",
            "distillation",
            "instruction",
            "dataset",
            "preference data",
            "data quality",
        ),
        "fallback_papers": [
            ("Self-Instruct", "https://arxiv.org/abs/2212.10560"),
            ("Alpaca", "https://crfm.stanford.edu/2023/03/13/alpaca.html"),
            ("Magpie", "https://arxiv.org/abs/2406.08464"),
        ],
        "anchors": [
            ("Hugging Face Datasets", "https://huggingface.co/docs/datasets"),
            ("Argilla docs", "https://docs.argilla.io/"),
            ("Datatrove", "https://github.com/huggingface/datatrove"),
        ],
    },
]


def normalize(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def md(value: str) -> str:
    return normalize(value).replace("|", r"\|")


def retry_delay(exc: urllib.error.HTTPError, attempt: int) -> float:
    retry_after = exc.headers.get("Retry-After")
    if retry_after and retry_after.isdigit():
        return float(retry_after)
    if exc.code == 429:
        return 15.0 * (attempt + 1)
    return 3.0 * (attempt + 1)


def fetch_arxiv(query: str, max_results: int = MAX_RESULTS_PER_TRACK) -> list[dict[str, str]]:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": "0",
            "max_results": str(max_results),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{params}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "github-profile-frontier-radar/2.0"},
    )
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
                root = ET.fromstring(response.read())
            break
        except urllib.error.HTTPError as exc:
            last_error = exc
            if attempt + 1 < MAX_RETRIES:
                time.sleep(retry_delay(exc, attempt))
        except (TimeoutError, urllib.error.URLError) as exc:
            last_error = exc
            if attempt + 1 < MAX_RETRIES:
                time.sleep(3 * (attempt + 1))
    else:
        raise RuntimeError(f"arXiv request failed after retries: {last_error}")

    papers: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title_el = entry.find("atom:title", ATOM_NS)
        id_el = entry.find("atom:id", ATOM_NS)
        published_el = entry.find("atom:published", ATOM_NS)
        summary_el = entry.find("atom:summary", ATOM_NS)
        if title_el is None or id_el is None or published_el is None:
            continue
        papers.append(
            {
                "title": normalize(title_el.text or ""),
                "url": normalize(id_el.text or ""),
                "date": normalize((published_el.text or "")[:10]),
                "summary": normalize(summary_el.text or "") if summary_el is not None else "",
            }
        )
    return papers


def filter_papers(
    track: dict[str, object],
    papers: list[dict[str, str]],
    limit: int = MAX_PAPERS_PER_TRACK,
) -> list[dict[str, str]]:
    needles = tuple(str(needle).lower() for needle in track["needles"])
    kept: list[dict[str, str]] = []
    for paper in papers:
        text = f"{paper['title']} {paper.get('summary', '')}".lower()
        if any(needle in text for needle in needles):
            kept.append(paper)
        if len(kept) == limit:
            break
    return kept


def format_links(items: list[tuple[str, str]], limit: int | None = None) -> str:
    selected = items[:limit] if limit is not None else items
    return "<br>".join(f"[{md(title)}]({url})" for title, url in selected)


def format_papers(track: dict[str, object], papers: list[dict[str, str]]) -> str:
    if papers:
        return "<br>".join(
            f"[{md(paper['title'])}]({paper['url']}) ({paper['date']})"
            for paper in papers
        )
    return format_links(track["fallback_papers"], limit=3)  # type: ignore[arg-type]


def render_radar() -> str:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"_Updated on {today} UTC. Recent arXiv papers are filtered by track; implementation anchors keep the radar useful when a topic is quiet or rate-limited._",
        "",
        "| Track | Recent papers | Implementation anchors |",
        "| --- | --- | --- |",
    ]

    for index, track in enumerate(TRACKS):
        label = str(track["label"])
        query = str(track["query"])
        try:
            papers = fetch_arxiv(query)
        except Exception as exc:
            print(f"warning: failed to fetch {label}: {exc}", file=sys.stderr)
            papers = []
        if index + 1 < len(TRACKS):
            time.sleep(ARXIV_DELAY_SECONDS)

        papers = filter_papers(track, papers)
        recent = format_papers(track, papers)
        anchors = format_links(track["anchors"], limit=4)  # type: ignore[arg-type]
        lines.append(f"| {md(label)} | {recent} | {anchors} |")

    return "\n".join(lines)


def replace_section(readme: str, replacement: str) -> str:
    if START not in readme or END not in readme:
        raise RuntimeError("README is missing frontier radar markers.")
    before, rest = readme.split(START, 1)
    _, after = rest.split(END, 1)
    return f"{before}{START}\n{replacement}\n{END}{after}"


def main() -> int:
    readme = README.read_text(encoding="utf-8")
    updated = replace_section(readme, render_radar())
    README.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
