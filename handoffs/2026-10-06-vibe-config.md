# Vibe Config handoff — 2026-10-06

## Purpose

Continue the **personal vibe-config control plane** for the user's full Mac/tool stack inside `ogmachine/360-stack-curator`.

This work is broader than GitHub-star curation. The intended product is one durable control plane for discovering, understanding, configuring, comparing, auditing, consolidating, replacing, and safely extending every configurable tool on the user's system.

Do **not** treat this as a flat app inventory.

## Safety boundary

**Do not modify Hazel recovery data, live Hazel rules, or live app configuration while continuing this config project.**

The Hazel recovery is unresolved and is being handled separately in the originating chat.

Preserved Hazel recovery data currently lives at:

`/Users/zhenyabannerboy/Library/Application Support/Hazel Recovery/2026-10-06-final`

The vibe-config work must remain sandboxed/read-only against live configuration until its UI, persistence, safety, and apply gates are validated.

## Existing local prototype

Sandbox vault:

`/Users/zhenyabannerboy/vibe-config-sandbox`

Entry points:

- `VIBE CONFIG.md` — dashboard
- `vibe-config.base` — shared Obsidian Base views
- `system/global-policy.md` — global preference/inheritance layer
- `system/scan.py` — Mac inventory scanner
- `system/build_ui.py` — UI/enrichment generator
- `system/snapshot.json` — normalized observed-state snapshot
- `system/docs-map.json` — first-pass official docs/config/recipe/best-practice links
- `system/github-stars-all.tsv` — deduped starred repositories from both authenticated GitHub accounts
- `registry/` — generated local configurable-entity records
- `candidates/` — generated GitHub candidate records

The live `nodebook` vault was intentionally left untouched.

## Current observed inventory

Latest generated inventory contains approximately **14,346 local entities**.

First-class entity types include:

- app bundles
- dot-folder tools
- skills
- plugins/extensions
- hooks
- rules
- agents/subagents
- MCP servers
- commands
- models/providers
- workflows/automations
- templates/profiles/snippets
- config files
- LaunchAgents / LaunchDaemons
- Application Support roots
- macOS containers / group containers
- CLIs
- Homebrew direct installs, casks, and dependency-only formulae
- npm global tools
- uv tools
- GitHub CLI extensions

Important design rule: **anything independently configurable is a first-class entity**, even when it is a sub-tool inside another tool.

Examples:

- Hazel → watched folder → rule → actions
- Claude → MCP server → config
- Hermes → agent → skill → hook
- PopClip → extension
- Obsidian → plugin → plugin settings
- GitHub CLI → extension / alias / auth / config

## GitHub source

GitHub CLI was installed and verified during the build:

- binary: `/opt/homebrew/bin/gh`
- version observed: `2.102.0`
- active account: `ogmachine`
- additional authenticated account: `zhenyadolgova`

Both authenticated accounts exposed the same **669 starred repositories** at the time of import.

Stars are **candidate resources**, not installed tools.

Candidate roles include:

- install candidate
- plugin/skill/source candidate
- recipe/reference
- alternative/replacement
- consolidation candidate
- ignore

Do not auto-install starred repositories.

The first candidate-matching implementation produced false overlaps from generic names such as `skill`, `pr`, `index`, and `web`; matching was tightened afterward. Continue validating identity/overlap logic rather than trusting fuzzy-name similarity.

## Core product model

Use one canonical entity graph rather than separate trackers.

Recommended inheritance:

`global preference → capability/group policy → tool → sub-tool → explicit exception`

Every configurable entity should be able to expose:

- observed/current state
- desired state
- inherited preference
- explicit exception
- parent/child relationships
- capability/use-case tags
- config layer: native / extended / system
- config surface: UI / file / CLI / API / rule editor / etc.
- impact scope
- risk level
- provenance/install source
- docs/evidence links
- local prior-context links
- drift status
- triage/decision state
- alternative/overlap relationships
- suggested action
- last validation timestamp

## Native config vs extended setup

Keep these visibly separate.

**Native configuration**

Settings exposed by the tool itself, such as preferences, account options, notification settings, menu-bar/Dock behavior, startup behavior, model settings, privacy controls, update channels, etc.

**Extended setup**

Composable capabilities layered on top of the tool, such as:

- Hazel rules
- PopClip extensions
- Claude/Codex/Hermes skills
- hooks
- agents/subagents
- MCP servers
- custom commands
- watch folders
- workflows
- automations
- templates
- provider/model profiles

A user should be able to configure either layer independently while still seeing the relationship between them.

## Intended interaction modes

The same source data should support multiple views/modes without duplicating records:

- configure something new
- finish setup
- inspect one tool
- browse capabilities
- audit drift
- repair broken config
- consolidate overlaps
- compare / replace a tool
- review new installs
- review GitHub candidates
- debris sweep
- review background services
- review risky automations

## Global vibe preferences

The prototype includes a universal preference layer for settings that can sensibly inherit across tools.

Examples:

- background/login behavior
- notifications/noise
- menu-bar/Dock presence
- telemetry/analytics
- appearance/theme
- update policy
- beta/release channel
- idle CPU/RAM/battery behavior
- local-vs-cloud processing
- permission scope
- automatic file processing
- destructive/in-place mutation policy
- output organization
- install/update provenance policy

Tool-specific options should remain tool-specific when a universal abstraction would lose meaning.

## Smart interpretation requirement

The interface must not merely expose raw settings.

For every important option, provide:

1. what the setting does
2. what changing it means **for this user/system**
3. likely trade-offs
4. inherited recommendation
5. conflicts with other preferences/tools
6. whether the setting is reversible
7. preview of resulting state

Use chips/selectors/toggles and constrained inputs wherever possible rather than requiring prose.

## Safety / zero-trust requirements

The tool should make Hazel-style mistakes difficult or impossible.

High-risk entities include at minimum:

- recursive rules
- file moves/renames/deletes
- hooks
- LaunchAgents / LaunchDaemons
- filesystem-wide agents
- background watchers
- permission expansion
- automatic installers/updaters

Before offering live apply for high-risk changes, require:

1. visible affected scope / blast radius
2. previewed diff
3. bounded fixture/test run
4. rollback evidence/path
5. collision handling policy
6. explicit enabled/disabled state
7. post-apply validation

`matched` is not equivalent to `successfully mutated`; preserve that distinction in automation logs and validation.

Never classify an unmatched App Support/container item as safe debris from ownership-name matching alone.

## Debris model

Unmatched state should be labeled **debris candidate**, never automatically removed.

Before removal, reconcile at least:

- active processes
- installed app bundles
- package-manager receipts
- launch items
- related binaries
- recent modification/activity
- known config/state relationships
- backups/rollback implications

## Capability ownership / consolidation

Reuse the earlier stack principle from the user's existing `UTIL-20261001-01 — Apple utility capability stack` ticket:

> one default owner per capability, explicit fallbacks, avoid unintentional parallel overlap

The UI should make overlapping capability ownership obvious and support triage such as:

- primary
- fallback
- niche/conditional
- redundant
- candidate replacement
- retire

## Evidence and documentation layer

Each tool/sub-tool should support links to:

- official docs
- configuration reference/guide
- recipes/examples
- official best practices
- source/repository when relevant
- current version/release notes when material
- user's prior nodebook/ticket/context references

Source hierarchy:

1. current official documentation / canonical repo
2. observed local state
3. user's prior registry/tickets/notes
4. community examples/recommendations, clearly labeled

Do not silently treat old nodebook notes as current truth when official/current behavior differs.

First-pass docs were already added for high-value tools including Hazel, Claude, Ollama, Miyo, Clop, ImageOptim, MacWhisper, Comfy Desktop, CleanMyMac, Stats, QLMarkdown, uBlock Origin Lite, Apple Configurator, WhatsApp, stoic, HyperFrames, and GitHub CLI.

This evidence layer is **partial**, not complete.

## Existing user-context sources found in nodebook

Relevant prior local work includes at least:

- `App registry.md`
- `config-estate.md`
- `WF-20261006-03 — Inventory every config root on the Mac into the state Base.md`
- `UTIL-20261001-01 — Apple utility capability stack.md`
- various per-app registry notes
- config-eval tickets
- Hazel/file-automation safety work

Miyo remote search was attempted but rejected by its connected plan, so local nodebook files were used directly instead.

## Obsidian prototype

The sandbox currently uses a deliberately small isolated plugin set copied from the live vault:

- native Bases
- Meta Bind
- Dataview
- Advanced Bases
- Buttons
- Pretty Properties

Do not blindly copy the live `.obsidian` configuration or plugin sprawl.

Meta Bind JavaScript was disabled in the sandbox during isolation.

## Current UI state

The prototype includes views for:

- command center
- recent apps
- high-risk automation
- configurable sub-tools
- debris candidates
- GitHub shortlist
- all GitHub stars

Per-entity notes include parent/child drill-down and interactive triage/desired-state selectors.

### Important: UI is **not yet fully validated**

Do not call the current prototype production-ready.

Still required:

- open/render the sandbox in Obsidian
- validate Base syntax and all view rendering
- validate Meta Bind writes
- verify performance with 14k+ local records + candidate records
- verify preference persistence across rescans
- verify generated enrichment survives rescans
- test parent/child navigation
- test docs URL rendering
- confirm copied plugin dependencies
- confirm empty fields collapse cleanly
- confirm candidate/preview/live states are visually unambiguous
- confirm dangerous controls cannot be mistaken for normal preferences

## Required persistence behavior

Observed state and user intent are different layers.

A rescan may refresh **observed state**, but must never overwrite:

- user preference
- triage decision
- desired state
- explicit exception
- notes/rationale
- accepted capability owner

The scanner and UI generator need a merge/persistence contract before this becomes a durable tool.

## Requirements-validation status

Strong/implemented first pass:

- apps + dot-folder tools
- nested skills/plugins/hooks/rules/agents
- MCP/models/workflows/templates/profiles/config files
- LaunchAgents / LaunchDaemons
- package-manager tools
- App Support / containers
- debris candidate model
- native vs extended config distinction
- preference inheritance concept
- GitHub stars as candidate resources
- persistent-view concept
- safety-gate architecture

Partial:

- capability/use-case enrichment from docs
- analog/alternative app context
- docs/evidence coverage
- user-specific interpretation copy
- drift detection
- candidate scoring quality
- consolidation recommendations

Not yet validated:

- rendered UI
- interaction quality
- persistence across rescans
- safe live-apply path

## Next-chat priorities

1. **Do not rescan/rebuild blindly first.** Inspect the existing sandbox and generated files.
2. Establish a formal schema/SSOT inside this repo that can represent both local installed entities and external candidates.
3. Define separation between:
   - observed state
   - user intent/preferences
   - derived interpretation
   - external evidence/docs
4. Add a stable relationship model for parent/sub-tool and capability ownership.
5. Add a durable persistence/merge strategy before regenerating entity records.
6. Runtime-QA the Obsidian interface before calling it validated.
7. Improve candidate identity matching and consolidation scoring.
8. Expand official-doc/capability/use-case/analogy coverage incrementally.
9. Only after the above, design a gated live-apply layer.

## Acceptance criteria for the next implementation phase

A representative end-to-end flow should work for each of these cases:

- ordinary utility: Stats
- AI/agent app: Claude or Codex
- local service: Ollama
- nested dot-tool: Hermes
- CLI/package tool: GitHub CLI
- file transformer: Clop
- dangerous automation: Hazel **in simulation only**
- debris candidate
- GitHub install/resource candidate

For each case, prove:

`discover → explain → configure intent → preview → persistence → validation`

For hazardous automation, additionally prove:

`scope → fixture → diff → rollback → explicit apply gate`

## Handoff rule

Do not claim completion from generated files alone. A feature is complete only when its requirement, implementation, runtime behavior, and acceptance test are all traceable and pass.
