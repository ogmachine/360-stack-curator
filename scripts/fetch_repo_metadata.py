#!/usr/bin/env python3
"""Fetch GitHub metadata for the portfolio repos and export a JSON dataset."""

import argparse
import json
import os
from urllib import error, request


def gh_json(url):
    req = request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "portfolio-automation/1.0",
        },
    )
    with request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def github_content_exists(owner, repo, path, ref):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={ref}"
    try:
        gh_json(url)
        return True
    except error.HTTPError:
        return False
    except Exception:
        return False


def fetch_repo_metadata(owner, repo_name):
    repo_url = f"https://api.github.com/repos/{owner}/{repo_name}"
    repo_data = gh_json(repo_url)

    default_branch = repo_data.get("default_branch", "main")
    languages = gh_json(f"https://api.github.com/repos/{owner}/{repo_name}/languages")

    files = {
        "README.md": github_content_exists(owner, repo_name, "README.md", default_branch),
        "SECURITY.md": github_content_exists(owner, repo_name, "SECURITY.md", default_branch),
        "CODEOWNERS": github_content_exists(owner, repo_name, "CODEOWNERS", default_branch),
        "LICENSE": github_content_exists(owner, repo_name, "LICENSE", default_branch),
        "CONTRIBUTING.md": github_content_exists(owner, repo_name, "CONTRIBUTING.md", default_branch),
    }

    return {
        "name": repo_data.get("name"),
        "full_name": repo_data.get("full_name"),
        "description": repo_data.get("description") or "",
        "language": repo_data.get("language"),
        "languages": languages,
        "private": repo_data.get("private", False),
        "archived": repo_data.get("archived", False),
        "fork": repo_data.get("fork", False),
        "created_at": repo_data.get("created_at"),
        "updated_at": repo_data.get("updated_at"),
        "pushed_at": repo_data.get("pushed_at"),
        "size": repo_data.get("size", 0),
        "open_issues_count": repo_data.get("open_issues_count", 0),
        "default_branch": default_branch,
        "has_readme": files["README.md"],
        "has_security": files["SECURITY.md"],
        "has_codeowners": files["CODEOWNERS"],
        "has_license": files["LICENSE"],
        "has_contributing": files["CONTRIBUTING.md"],
    }


def load_repo_names(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg["repo_list"]


def main():
    parser = argparse.ArgumentParser(description="Fetch repo metadata for the portfolio.")
    parser.add_argument("--owner", required=True, help="GitHub owner/organization")
    parser.add_argument("--config", default="config/portfolio-rules.json", help="JSON config with repo list")
    parser.add_argument("--output", default="data/portfolio_repo_metadata.json", help="Output JSON path")
    args = parser.parse_args()

    repo_names = load_repo_names(args.config)
    metadata = []
    for repo_name in repo_names:
        try:
            metadata.append(fetch_repo_metadata(args.owner, repo_name))
        except Exception as exc:  # pragma: no cover - network failure should be visible
            print(f"WARN: failed to fetch {args.owner}/{repo_name}: {exc}", file=os.sys.stderr)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"Fetched metadata for {len(metadata)} repos -> {args.output}")


if __name__ == "__main__":
    main()
