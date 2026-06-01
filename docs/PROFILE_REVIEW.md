# Profile Review Notes

Last reviewed: 2026-06-01 UTC

This document records the design review behind the profile README. It is meant to keep future edits from drifting into a badge wall, link dump, or vague AI slogan page.

## Sources Checked

| Source | Takeaway used in the profile |
| --- | --- |
| [GitHub: Managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) | The profile README is rendered from a public `Ruazzm/Ruazzm` repository with a non-empty root `README.md`. |
| [GitHub: About your profile](https://docs.github.com/en/account-and-profile/concepts/personal-profile) | A profile should showcase work, contributions, and useful public context. Contributions the author is proud of are explicitly good profile material. |
| [GitHub: Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | Mermaid diagrams are supported in Markdown files, so a compact operating loop is safe to keep in the README. |
| [arXiv API User Manual](https://info.arxiv.org/help/api/user-manual.html) | Automated radar requests should use small result sets and include a delay between calls. |
| [karpathy profile](https://github.com/karpathy) | Very short positioning works when the pinned work already carries the depth. |
| [simonw profile](https://github.com/simonw) | Self-updating profile sections are strongest when they surface real recent work rather than generic stats. |
| [hamelsmu profile](https://github.com/hamelsmu) | A direct statement of current work is more useful than a long technology list. |

## Findings

| Area | Previous issue | Change made |
| --- | --- | --- |
| First-screen credibility | The page had strong taste, but little directly verifiable work near the top. | Added a `Current Public Work` section with recent upstream LLaMA-Factory PRs and maintained docs/workflow links. |
| Information hierarchy | The reading map was useful but competed with the core identity of the profile. | Reframed the profile around public work, workbench, operating loop, research shelf, and publish standard. |
| Aspirational content | Planned repo names appeared as if they were current artifacts. | Moved planned artifacts into a collapsed section and named them as future inspectable repos. |
| Literature scope | Early versions leaned too much toward foundation-model release anchors. | Expanded tracks to post-training, evals, agents, RAG, inference, multimodal/documents, and data/distillation. |
| Automation robustness | The radar script worked but had little visible rate-limit discipline. | Added constants, retry-after handling, request spacing, workflow concurrency, and a job timeout. |
| Page aesthetics | Too many dense tables can make a profile feel like a database. | Kept only high-signal tables on the main page and pushed the long shelf to `TECHNICAL_READING_MAP.md`. |

## Current Positioning

The profile should signal:

- real upstream code and documentation work,
- interest in post-training and LLM systems beyond base-model releases,
- preference for evidence-rich experiments,
- awareness of evaluation, retrieval, serving, and data pipeline details,
- and a habit of maintaining a technical reading map.

## Future Review Checklist

- Does the first screen still contain real public work?
- Are planned artifacts clearly marked as planned?
- Are there any dead links or references to stale model releases?
- Is the README still readable without opening collapsed sections?
- Does the frontier radar add signal, or is it committing date-only churn?
- Are the pinned repositories aligned with the profile's stated workbench?
