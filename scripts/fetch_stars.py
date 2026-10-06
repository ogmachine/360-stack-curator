#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

try:
    import requests
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"Missing dependency: {exc}. Install with: python -m pip install requests")


def fetch_starred_repos(token: str, per_page: int = 100):
    """Fetch starred repos for the authenticated user."""
    repos = []
    page = 1
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
    }
    while True:
        url = f"https://api.github.com/user/starred?per_page={per_page}&page={page}"
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1
    return repos


def normalize_repo(repo):
    return {
        "name": repo.get("name"),
        "owner": repo.get("owner", {}).get("login"),
        "full_name": repo.get("full_name"),
        "url": repo.get("html_url"),
        "description": repo.get("description"),
        "language": repo.get("language"),
        "stars": repo.get("stargazers_count", 0),
        "resourceType": "unknown",
        "categories": [],
        "capabilities": [],
        "agentCompatibility": {},
        "deploymentTier": "use-case-specific",
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub starred repos for the authenticated user.")
    parser.add_argument("--output", default="data/repos.json", help="Output JSON path")
    args = parser.parse_args()

    # Get token from environment variable
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise SystemExit("Error: GITHUB_TOKEN environment variable not set. Set it with: export GITHUB_TOKEN='your_token_here'")

    items = fetch_starred_repos(token)
    normalized = [normalize_repo(repo) for repo in items]

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(normalized, indent=2), encoding="utf-8")
    print(f"Fetched {len(normalized)} repos to {out_path}")


if __name__ == "__main__":
    main()
