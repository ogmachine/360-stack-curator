# Archive and sunsetting policy

This document defines when a repo should be archived, deprecated, or moved into a sandbox model.

## Purpose

The portfolio should stay lean, intentionally structured, and easy to reason about. A repo should not remain active just because it exists.

## Archive criteria

Archive a repo when all of the following are true:

- there is no clear owner
- there is no clear roadmap value
- there is no meaningful documentation or maintenance signal
- it has become redundant or superseded
- it has no active product or platform purpose

## Deprecate criteria

Deprecate a repo when:

- it has been replaced by a better design or active repo
- it remains only as historical context
- it is conceptually useful but not operationally active

## Sandbox criteria

Move a repo to sandbox status when:

- it is still useful as an experiment or proof of concept
- it has limited strategic value
- it remains active but not core to the roadmap
- it needs lighter governance and less formal review

## Recommended archive decisions for this portfolio

### Strong candidates for lightweight sandbox or archive review
- ogmachine/soundwave-showcase
- ogmachine/kizuna-dance
- ogmachine/probable-doodle
- ogmachine/remix-of-lovable-slides
- ogmachine/skill-sequence-manager

These repos may continue as experiments if they are still useful. Otherwise, they should be archived after review.

### Do not archive without review
- ogmachine/360-stack-curator
- ogmachine/brandable-slides-studio
- ogmachine/operating-studio
- ogmachine/design-system-starter-kit

These are the strongest strategic and platform candidates.

## Process for archive decisions

1. Review repo purpose and owner.
2. Confirm roadmap relevance.
3. Check whether the repo has active maintenance or issue flow.
4. Decide whether to archive, deprecate, or keep in sandbox.
5. Update README and repo status in the portfolio catalog.
6. Record the decision in the decision log or roadmap notes.

## Practical policy

A repo should not remain in the active portfolio indefinitely without:

- a clear purpose
- an active owner
- a roadmap or maintenance reason
- a validation and review path

## Final principle

The portfolio is healthier when it is lean and intentional than when it is large and ambiguous.
