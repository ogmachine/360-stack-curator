# Portfolio implementation checklist

This checklist turns the governance model into a working execution plan for the repo portfolio.

## Phase 1: classify and assign ownership

### Required for all repos
- [ ] Classify repo as strategic / shared platform / showcase / prototype / archive
- [ ] Assign product owner
- [ ] Assign technical owner
- [ ] Assign maintainer or active reviewer
- [ ] Add repo to the catalog
- [ ] Record lifecycle status
- [ ] Link to roadmap item or note if none exists

### Current portfolio classification
- [ ] 360-stack-curator -> Strategic product
- [ ] brandable-slides-studio -> Strategic product
- [ ] operating-studio -> Shared platform
- [ ] design-system-starter-kit -> Shared platform
- [ ] zd_portfolio -> Portfolio/showcase
- [ ] soundwave-showcase -> Portfolio/showcase
- [ ] kizuna-dance -> Portfolio/showcase
- [ ] skill-sequence-manager -> Prototype
- [ ] remix-of-lovable-slides -> Prototype
- [ ] probable-doodle -> Prototype

## Phase 2: apply repo standards to active repos

### For strategic and shared-platform repos
- [ ] README.md exists and states purpose clearly
- [ ] CONTRIBUTING.md exists
- [ ] SECURITY.md exists
- [ ] CODEOWNERS exists
- [ ] LICENSE is present if required
- [ ] issue templates exist
- [ ] PR template exists
- [ ] branch protection enabled
- [ ] review required before merge
- [ ] status checks required
- [ ] labels configured
- [ ] roadmap linkage recorded

### For showcase repos
- [ ] README exists
- [ ] owner assigned
- [ ] issue flow enabled
- [ ] basic branch protections enabled
- [ ] roadmap or keep decision documented

### For prototype repos
- [ ] README exists
- [ ] owner assigned
- [ ] lightweight issue flow enabled
- [ ] quarterly review scheduled

## Phase 3: roadmap alignment

- [ ] Create a top-level roadmap document
- [ ] Map each active repo to one strategic initiative or product lane
- [ ] Ensure each roadmap item has owner and issue link
- [ ] Ensure each task has validation evidence
- [ ] Record milestones and priorities

## Phase 4: archive and prune review

### Review candidates
- [ ] probable-doodle
- [ ] remix-of-lovable-slides
- [ ] soundwave-showcase
- [ ] kizuna-dance
- [ ] skill-sequence-manager

### Decision rules
- [ ] Keep if meaningful and active
- [ ] Move to sandbox if exploratory but still useful
- [ ] Archive if no owner, no value, no roadmap fit, or no active maintenance

## Phase 5: cross-agent workflow adoption

- [ ] Use issue-first workflow for meaningful work
- [ ] Require handoff template for agent transitions
- [ ] Require validation evidence before completion
- [ ] Require docs update when behavior or workflow changes
- [ ] Escalate uncertain or risky changes to human owner

## Repo-by-repo action plan

### 1) 360-stack-curator
- [ ] Confirm as portfolio control plane
- [ ] Keep as central governance repo
- [ ] Maintain README and docs
- [ ] Keep roadmap and repo catalog updated

### 2) brandable-slides-studio
- [ ] Confirm product purpose
- [ ] Add README and repo standard docs
- [ ] Define product owner
- [ ] Link to roadmap initiative

### 3) operating-studio
- [ ] Confirm role as ops/governance layer
- [ ] Add ownership and repo hygiene baseline
- [ ] Create design docs if not present

### 4) design-system-starter-kit
- [ ] Confirm as shared platform foundation
- [ ] Add README and CODEOWNERS
- [ ] Ensure clear contribution workflow

### 5) zd_portfolio
- [ ] Keep as portfolio/showcase
- [ ] Set lightweight governance and owner
- [ ] Decide if it is active strategic showcase or a personal site

### 6) soundwave-showcase
- [ ] Decide whether it is active showcase or sandbox
- [ ] Add owner and README if kept
- [ ] Otherwise move to archive review

### 7) kizuna-dance
- [ ] Decide whether it is active event or campaign work
- [ ] Add minimal owner and README if retained
- [ ] Otherwise move to sandbox/archive review

### 8) skill-sequence-manager
- [ ] Clarify whether it is a learning-system concept or a real product
- [ ] Add clear README and owner
- [ ] Decide keep as prototype or archive

### 9) remix-of-lovable-slides
- [ ] Keep only if there is a clear derivative product goal
- [ ] Otherwise archive as prototype exploration

### 10) probable-doodle
- [ ] Treat as prototype/sandbox
- [ ] Review quarterly for archive or keep

## Success criteria

The initiative is successful when:

- every repo has a status
- every repo has an owner
- all strategic repos have repo hygiene baseline
- roadmap items are issue-linked and reviewable
- prototype repos are intentionally managed rather than left ambiguous
- archive and sandbox decisions are documented
- agents have a clear operating model and safe boundaries

## Recommended next milestone

Complete the ownership and repo standard review for the four strategic repos first, then apply lighter governance to the showcase and prototype repos.

This creates a stable operating foundation without over-investing in low-value experiments.
