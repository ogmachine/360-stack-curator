#!/usr/bin/env python3
"""Classify portfolio repos from GitHub metadata and write a status board."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def compute_status(repo, config):
    score = 0
    name_lower = (repo.get("name") or "").lower()
    description = (repo.get("description") or "").strip()
    languages = repo.get("languages") or {}
    primary_lang = repo.get("language") or ""

    if description:
        score += 2
    if repo.get("has_readme"):
        score += 3
    if repo.get("has_security"):
        score += 2
    if repo.get("has_codeowners"):
        score += 2
    if repo.get("has_license"):
        score += 1
    if repo.get("has_contributing"):
        score += 1
    if primary_lang in {"TypeScript", "Python"}:
        score += 2
    if primary_lang in {"HTML", "JavaScript"}:
        score += 1

    if repo.get("name") in config["strategic_repos"]:
        score += 4
    elif repo.get("name") in config["showcase_repos"]:
        score += 2
    elif repo.get("name") in config["prototype_repos"]:
        score += 0

    if "studio" in name_lower or "curator" in name_lower or "system" in name_lower or "manager" in name_lower:
        score += 1
    if "doodle" in name_lower or "remix" in name_lower or "showcase" in name_lower:
        score -= 1

    pushed_at = parse_date(repo.get("pushed_at"))
    if pushed_at:
        age_days = (datetime.now(timezone.utc) - pushed_at).days
        if age_days <= 90:
            score += 2
        elif age_days > 180:
            score -= 2

    if repo.get("open_issues_count", 0) > 0:
        score += 1

    reasons = []
    if description:
        reasons.append("clear description")
    if repo.get("has_readme"):
        reasons.append("README present")
    if repo.get("has_security"):
        reasons.append("security policy present")
    if repo.get("name") in config["strategic_repos"]:
        reasons.append("strategic repo")
    if repo.get("name") in config["showcase_repos"]:
        reasons.append("showcase repo")
    if repo.get("name") in config["prototype_repos"]:
        reasons.append("prototype repo")
    if pushed_at:
        age_days = (datetime.now(timezone.utc) - pushed_at).days
        if age_days <= 90:
            reasons.append("recent activity")

    threshold_strategic = config["thresholds"].get("strategic", 10)
    threshold_showcase = config["thresholds"].get("showcase", 6)
    threshold_sandbox = config["thresholds"].get("sandbox", 3)

    if repo.get("name") in config["strategic_repos"] and score >= threshold_strategic:
        status = "Strategic"
        action = "Apply full governance baseline"
        decision = "Keep"
    elif repo.get("name") in config["showcase_repos"] or score >= threshold_showcase:
        status = "Showcase"
        action = "Review keep vs sandbox"
        decision = "Keep or sandbox"
    elif repo.get("name") in config["prototype_repos"] or score >= threshold_sandbox:
        status = "Sandbox"
        action = "Review quarterly and decide keep or archive"
        decision = "Sandbox or archive"
    elif score < config["thresholds"].get("archive", 2):
        status = "Archive"
        action = "Recommend archive or deprecate"
        decision = "Archive"
    else:
        status = "Sandbox"
        action = "Review quarterly and decide keep or archive"
        decision = "Sandbox or archive"

    return {
        "name": repo.get("name"),
        "score": score,
        "status": status,
        "action": action,
        "decision": decision,
        "reasons": ", ".join(reasons) if reasons else "insufficient detail",
    }


def markdown_table(rows):
    headers = ["Repo", "Status", "Score", "Owner", "Next action", "Decision"]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["status"],
                    str(row["score"]),
                    "ogmachine",
                    row["action"],
                    row["decision"],
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Classify portfolio repos and regenerate the status board.")
    parser.add_argument("--metadata", required=True, help="JSON metadata file from fetch_repo_metadata.py")
    parser.add_argument("--config", default="config/portfolio-rules.json", help="Portfolio config JSON")
    parser.add_argument("--output", default="docs/portfolio-status-board.md", help="Output markdown board path")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)
    with open(args.metadata, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    rows = []
    for repo in metadata:
        result = compute_status(repo, config)
        rows.append(result)

    doc = "# Portfolio status board\n\n"
    doc += "This status board is generated from the latest GitHub metadata and repo health signals.\n\n"
    doc += markdown_table(rows)
    doc += "\n\n## Classification rules\n\n"
    doc += "- Strategic: high-product-value and well-governed repos\n"
    doc += "- Showcase: still valuable but not core product/platform work\n"
    doc += "- Sandbox: exploratory or lower-priority repos\n"
    doc += "- Archive: low purpose clarity, stale, or no meaningful maintenance\n"

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(doc + "\n", encoding="utf-8")

    print(f"Wrote {len(rows)} repo classifications to {out_path}")


if __name__ == "__main__":
    main()
