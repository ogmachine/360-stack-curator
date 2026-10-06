# 360 Stack Curator

A curated, data-driven stack intelligence project for your GitHub starred repositories.

This project is designed to help you:

- understand what tools and repos you actually keep around
- map your starred repos to capabilities, domains, and resource types
- compare repos across multiple AI agents and local runtimes
- see overlaps, gaps, and duplication across your stack
- design a universal vs. conditional architecture for routing, discoverability, and best-fit tooling

## What this project contains

- `schema/` — JSON schema for repos, capabilities, and agents
- `data/` — starter taxonomy and agent compatibility data
- `scripts/` — ingestion and build scripts
- `README.md` — project overview and usage notes

## Quick start

1. Install Python dependencies if needed:
   ```bash
   python -m pip install requests
   ```

2. Fetch your starred repos:
   ```bash
   python scripts/fetch_stars.py --user ogmachine --output data/repos.json
   ```

3. Build the initial capability summary:
   ```bash
   python scripts/build_stack.py --repos data/repos.json --output data/stack-summary.json
   ```

4. Review the generated summaries in `data/`.

## Core model

The project uses three core objects:

- `repo`: a GitHub repository or tool footprint
- `capability`: a domain/feature a repo supports
- `agent`: a target agent runtime or platform (Claude Code, ChatGPT, Hermes, Gemini, local agent, etc.)

## File structure

```text
360-stack-curator/
├── README.md
├── schema/
│   ├── repo.schema.json
│   ├── capability.schema.json
│   └── agent.schema.json
├── data/
│   ├── capability-taxonomy.json
│   ├── agent-matrix.json
│   ├── architecture.yaml
│   ├── repos.json
│   └── stack-summary.json
├── scripts/
│   ├── fetch_stars.py
│   └── build_stack.py
└── exports/
    └── .gitkeep
```

## Planned outputs

This project is designed to support multiple interfaces:

- Airtable-like tables for easy review and editing
- Obsidian-like graph views for context and relationship mapping
- standalone dashboard or local app for scoring and architecture analysis

## Notes

This is intentionally a hybrid project: a source-of-truth dataset with scripts and exports, plus a graph-friendly architecture for future visualization.

Use the generated JSON as the single source of truth, then render it into a table, graph, or app layer.

## Project goals

- capture and normalize your starred tools and codified knowledge
- reveal overlaps, gaps, and duplicate functionality
- map each repo to capabilities and domains
- show what is universal vs agent-specific vs conditional
- suggest a practical architecture for routing, discoverability, and tool fit
