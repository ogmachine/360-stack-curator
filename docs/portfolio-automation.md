# Portfolio automation system

This folder contains the lightweight automation used to keep the repo portfolio aligned with the operating model.

## Workflow

1. Fetch fresh GitHub metadata for the portfolio repos.
2. Classify each repo using the scoring model in `scripts/classify_repos.py`.
3. Update the status board and identify actions that need human attention.
4. Use the generated board to decide which repos should be kept, sandboxed, or archived.

## Commands

```bash
python scripts/fetch_repo_metadata.py --owner ogmachine --config config/portfolio-rules.json --output data/portfolio_repo_metadata.json
python scripts/classify_repos.py --metadata data/portfolio_repo_metadata.json --config config/portfolio-rules.json --output docs/portfolio-status-board.md
```

## What the automation checks

- repo description and purpose clarity
- primary language and technical profile
- README, security, CODEOWNERS, LICENSE, and contributing policy presence
- recent repo activity
- strategic vs showcase vs prototype classification
- archive candidates

## Why this matters

This keeps the portfolio running without constant manual review. The data-driven classification is more consistent than ad hoc human judgement and creates a traceable operating rhythm.
