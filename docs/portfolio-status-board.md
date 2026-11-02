# Portfolio status board

This is the working operational board for the repo portfolio. It defines the current status, category, next action, and lifecycle decision for each repository.

## Status definitions

- Strategic: active and important to roadmap or product direction
- Shared platform: foundational repo used by or supporting other work
- Showcase: active but not a core product or platform dependency
- Sandbox: exploratory or lower-priority but still deliberately retained
- Archived: intentionally retired or scheduled for deprecation

## Current repo status

| Repo | Category | Status | Owner | Next action | Decision |
| --- | --- | --- | --- | --- | --- |
| ogmachine/360-stack-curator | Strategic product | Strategic | ogmachine | Keep as control plane and governance anchor | Keep |
| ogmachine/brandable-slides-studio | Strategic product | Strategic | ogmachine | Confirm product intent and add repo hygiene baseline | Keep |
| ogmachine/operating-studio | Shared platform | Strategic | ogmachine | Confirm workflow/ops role and repository standards | Keep |
| ogmachine/design-system-starter-kit | Shared platform | Strategic | ogmachine | Add README, CODEOWNERS, and contribution rules | Keep |
| ogmachine/zd_portfolio | Showcase | Showcase | ogmachine | Decide if this is active portfolio work or personal site | Keep or sandbox |
| ogmachine/soundwave-showcase | Showcase | Sandbox | ogmachine | Review value and whether it should remain as creative showcase | Sandbox or archive |
| ogmachine/kizuna-dance | Showcase | Sandbox | ogmachine | Review use case and keep only if still meaningful | Sandbox or archive |
| ogmachine/skill-sequence-manager | Prototype | Sandbox | ogmachine | Clarify actual product intent and roadmap value | Keep or archive |
| ogmachine/remix-of-lovable-slides | Prototype | Sandbox | ogmachine | Confirm if this is a derivative product path or experiment | Archive if no clear value |
| ogmachine/probable-doodle | Prototype | Sandbox | ogmachine | Keep only as a low-cost experimentation repo | Archive if inactive |

## Immediate next actions

### Strategic repos: apply full governance baseline
- ogmachine/360-stack-curator
- ogmachine/brandable-slides-studio
- ogmachine/operating-studio
- ogmachine/design-system-starter-kit

Required actions:
- confirm purpose in README
- assign owner and maintainer
- enforce branch protection
- add issue and PR templates
- add CODEOWNERS and SECURITY
- attach roadmap or initiative link
- validate repo health

### Showcase repos: decide active vs sandbox
- ogmachine/zd_portfolio
- ogmachine/soundwave-showcase
- ogmachine/kizuna-dance

Required actions:
- decide whether they are active brand or portfolio assets
- add lightweight owner and README if kept
- move to sandbox or archive if not worth active attention

### Prototype repos: review and decide
- ogmachine/skill-sequence-manager
- ogmachine/remix-of-lovable-slides
- ogmachine/probable-doodle

Required actions:
- verify whether there is a real product or learning path
- archive if there is no concrete use case or owner
- keep only if there is a real direction and future value

## Review cadence

- Weekly: review strategic repo status
- Monthly: review roadmap and owner status
- Quarterly: run full keep / sandbox / archive decision review for showcase and prototype repos

## Decision rule

A repo remains active if it has all of the following:

- clear purpose
- active owner
- roadmap or maintenance reason
- basic documentation
- no ambiguity in value or ownership

Otherwise it should be moved to sandbox or archive.
