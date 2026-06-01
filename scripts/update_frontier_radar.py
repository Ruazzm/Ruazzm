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


TOPICS = [
    (
        "Reasoning / RLVR",
        'cat:cs.CL AND (all:"reasoning" OR all:"verifiable reward" OR all:"test-time compute" OR all:"reinforcement learning")',
    ),
    (
        "Agents / tool use",
        'cat:cs.CL AND (all:"agent" OR all:"tool use" OR all:"computer use" OR all:"MCP")',
    ),
    (
        "RAG / memory",
        'cat:cs.CL AND (all:"retrieval augmented generation" OR all:"GraphRAG" OR all:"memory")',
    ),
    (
        "Inference / serving",
        'cat:cs.CL AND (all:"speculative decoding" OR all:"KV cache" OR all:"long context" OR all:"efficient inference")',
    ),
    (
        "Multimodal models",
        'cat:cs.CL AND (all:"multimodal" OR all:"video understanding" OR all:"vision language model")',
    ),
]


FALLBACK_SIGNALS = {
    "Reasoning / RLVR": [
        ("DeepSeek-R1: reasoning via reinforcement learning", "https://arxiv.org/abs/2501.12948"),
        ("s1: simple test-time scaling", "https://arxiv.org/abs/2501.19393"),
        ("Qwen3: hybrid thinking modes", "https://qwenlm.github.io/blog/qwen3/"),
    ],
    "Agents / tool use": [
        ("Anthropic Claude 4: extended thinking and tool use", "https://www.anthropic.com/news/claude-4"),
        ("Model Context Protocol", "https://www.anthropic.com/news/model-context-protocol"),
    ],
    "RAG / memory": [
        ("Microsoft GraphRAG", "https://www.microsoft.com/en-us/research/project/graphrag/"),
        ("Contextual retrieval", "https://www.anthropic.com/news/contextual-retrieval"),
    ],
    "Inference / serving": [
        ("Speculative decoding", "https://arxiv.org/abs/2211.17192"),
        ("vLLM paged attention", "https://arxiv.org/abs/2309.06180"),
    ],
    "Multimodal models": [
        ("Qwen3: hybrid thinking modes", "https://qwenlm.github.io/blog/qwen3/"),
        ("Llama 4: native multimodal MoE models", "https://ai.meta.com/blog/llama-4-multimodal-intelligence/"),
        ("Gemini 3.1 Pro model card", "https://deepmind.google/models/model-cards/gemini-3-1-pro"),
    ],
}


def normalize(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def fetch_arxiv(query: str, max_results: int = 3) -> list[dict[str, str]]:
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
        headers={"User-Agent": "github-profile-frontier-radar/1.0"},
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                root = ET.fromstring(response.read())
            break
        except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as exc:
            last_error = exc
            time.sleep(5 * (attempt + 1))
    else:
        raise RuntimeError(f"arXiv request failed after retries: {last_error}")

    papers: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title_el = entry.find("atom:title", ATOM_NS)
        id_el = entry.find("atom:id", ATOM_NS)
        published_el = entry.find("atom:published", ATOM_NS)
        if title_el is None or id_el is None or published_el is None:
            continue
        papers.append(
            {
                "title": normalize(title_el.text or ""),
                "url": normalize(id_el.text or ""),
                "date": normalize((published_el.text or "")[:10]),
            }
        )
    return papers


def render_radar() -> str:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"_Auto-updated on {today} UTC from arXiv recent submissions._",
        "",
        "| Track | Fresh signals |",
        "| --- | --- |",
    ]

    for label, query in TOPICS:
        try:
            papers = fetch_arxiv(query)
        except Exception as exc:
            print(f"warning: failed to fetch {label}: {exc}", file=sys.stderr)
            papers = []
        time.sleep(3.2)

        if papers:
            items = [
                f"[{paper['title']}]({paper['url']}) ({paper['date']})"
                for paper in papers
            ]
            signals = "<br>".join(items)
        else:
            fallback_items = [
                f"[{title}]({url})" for title, url in FALLBACK_SIGNALS.get(label, [])
            ]
            signals = "Curated fallback: " + "<br>".join(fallback_items)
        lines.append(f"| {label} | {signals} |")

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
