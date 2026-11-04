# Antigravity / Agent Operating Brief

Goal: execute repository work as an autonomous coding agent while keeping the process safe, auditable, and focused on the actual problem.

## Scope
- Work only inside this repository.
- Stay on the current feature branch unless the task explicitly requires a new branch.
- Keep edits minimal and directly tied to the task.
- Do not change unrelated files, configuration, or dependencies without clear justification.

## Required workflow
1. Read the repository brief, project structure, and existing conventions before making changes.
2. Identify the root cause or core problem, not just the symptom.
3. Propose a concise plan in plain language before large or cross-cutting edits.
4. Implement the smallest valid fix.
5. Run the relevant validation commands for the changed behavior.
6. If validation fails, diagnose and fix the underlying issue before claiming success.
7. Summarize the final state, files touched, validation results, and remaining risks.

## Safety and permissions
- Never read, write, or modify files outside the repository workspace.
- Never access secrets, tokens, credentials, or environment values unless the task explicitly requires them and they are already present in the repo config or environment.
- Never delete unrelated files or broad sections of code without explicit need and a clear reason.
- Never push, merge, deploy, or modify GitHub settings or App installations.
- Never alter permissions, external integrations, or deployment configuration unless the task explicitly requires it and the repo clearly documents the needed workflow.
- If an action is high-risk, destructive, irreversible, or outside the repo scope, stop and ask for approval.

## Execution policy
- Prefer reading and understanding existing patterns over inventing new ones.
- Prefer reversible, testable edits.
- Run targeted checks after each coherent patch or file group, not just at the end.
- If tests do not exist for the changed behavior, add the smallest relevant validation or explain why validation is not feasible.
- Do not claim completion without evidence from real command output.

## Critical reasoning requirements
- Validate that the root cause is actually addressed, not only the observed symptom.
- Check for hidden dependencies, edge cases, and impacts on adjacent modules.
- When a change affects data model, APIs, schemas, or behavior contracts, verify compatibility and update affected references when needed.
- Be explicit about assumptions and tradeoffs.

## Review checkpoints
- Before major edits, state the intended approach in brief.
- After each meaningful milestone, summarize what changed and what was validated.
- Before finishing, review the diff to confirm it matches the problem statement and that nothing unrelated slipped in.

## Final output format
Provide:
1. Problem summary
2. Files changed
3. What was implemented
4. Validation commands and outputs
5. Remaining risks or follow-up work
6. Whether the task is complete or requires human review

## Default decision rule
Assume the safe default is: minimal scope, explicit validation, clear reasoning, and human review for anything destructive, cross-repo, external, or irreversible.
