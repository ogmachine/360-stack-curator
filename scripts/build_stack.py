#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CAPABILITY_HINTS = {
    "agent": ["agent-orchestration", "skill-routing", "multi-agent-loop", "tool-invocation"],
    "langflow": ["agent-orchestration", "workflow-design"],
    "n8n": ["workflow-automation", "data-pipeline"],
    "dify": ["agent-orchestration", "workflow-design"],
    "llm": ["model-routing", "provider-fallback"],
    "litellm": ["model-routing", "provider-fallback"],
    "quivr": ["rag", "semantic-search"],
    "langchain": ["rag", "knowledge-graph"],
    "playwright": ["browser-automation", "web-scraping"],
    "browser-use": ["browser-automation"],
    "obsidian": ["notes-graph", "personal-wiki", "knowledge-management"],
    "foam": ["notes-graph", "personal-wiki"],
    "invokeai": ["image-generation", "creative-workflow"],
    "comfy": ["image-generation"],
    "voice": ["voice-generation"],
    "local": ["local-ai", "privacy-first", "self-hosting"],
    "docker": ["self-hosting", "devops"],
    "terraform": ["devops", "deployment"],
    "kubernetes": ["devops", "deployment"],
    "security": ["security-audit", "prompt-injection-detection"],
    "chatgpt": ["reasoning", "knowledge-work"],
    "claude": ["code-generation", "repo-analysis", "task-planning"],
    "codex": ["code-generation", "repo-analysis"],
    "gemini": ["document-ingestion", "research"],
    "notion": ["personal-wiki", "knowledge-management"],
    "dashboard": ["dashboard-ui", "internal-tooling"],
    "ui": ["dashboard-ui", "visual-builder"],
    "design": ["diagram-creation", "visual-builder"],
    "diagram": ["diagram-creation", "visual-builder"],
    "file": ["file-management"],
    "notes": ["personal-wiki", "notes-graph"],
    "knowledge": ["knowledge-graph", "rag"],
    "memory": ["memory-retention", "context-management"],
    "research": ["semantic-search", "document-ingestion"],
}


def infer_capabilities(repo):
    text = " ".join([
        (repo.get("name") or ""),
        (repo.get("description") or ""),
        (repo.get("language") or ""),
    ]).lower()

    capabilities = []
    for needle, hints in CAPABILITY_HINTS.items():
        if needle in text:
            capabilities.extend(hints)

    # Deduplicate while retaining order
    seen = set()
    ordered = []
    for cap in capabilities:
        if cap not in seen:
            seen.add(cap)
            ordered.append(cap)

    # Always ensure some minimal capability shape
    if not ordered:
        ordered = ["knowledge-work"]

    return ordered


def infer_resource_type(repo):
    text = " ".join([
        (repo.get("name") or ""),
        (repo.get("description") or ""),
    ]).lower()

    if any(k in text for k in ["agent", "claude", "codex", "openhands", "llm"]):
        return "agent-runtime"
    if any(k in text for k in ["langflow", "dify", "n8n", "workflow", "orchestr"]):
        return "workflow-orchestration"
    if any(k in text for k in ["obsidian", "note", "wiki", "knowledge", "foam"]):
        return "knowledge-base"
    if any(k in text for k in ["browser", "playwright", "automation"]):
        return "browser-tool"
    if any(k in text for k in ["image", "voice", "design", "diagram", "creative"]):
        return "creative-tool"
    if any(k in text for k in ["local", "self-host", "docker", "kubernetes", "devops"]):
        return "infrastructure"
    if any(k in text for k in ["dashboard", "admin", "ui"]):
        return "ui-tool"
    return "tooling"


def main():
    parser = argparse.ArgumentParser(description="Build a starter stack summary from repo metadata.")
    parser.add_argument("--repos", required=True, help="Path to a repos.json file")
    parser.add_argument("--output", default="data/stack-summary.json", help="Output path")
    args = parser.parse_args()

    repos = json.loads(Path(args.repos).read_text(encoding="utf-8"))

    summary = []
    for repo in repos:
        summary.append({
            "name": repo.get("name"),
            "owner": repo.get("owner"),
            "full_name": repo.get("full_name"),
            "url": repo.get("url"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "stars": repo.get("stars", 0),
            "resourceType": infer_resource_type(repo),
            "capabilities": infer_capabilities(repo),
            "deploymentTier": "use-case-specific",
        })

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Wrote {len(summary)} repo summaries to {out_path}")


if __name__ == "__main__":
    main()
