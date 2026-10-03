---
name: company-spec
description: Maintain Unboxers product and workflow specifications using OpenSpec-compatible requirements and scenarios. Use for company behavior changes, durable design choices, cross-repository contracts, or specification updates; keep trivial fixes lightweight and exclude personal work.
---

# Company Spec

Use one specification workflow instead of separate domain and decision writing workflows. Current behavior belongs in capability specs; change intent and technical choices belong in change artifacts. Read [references/writing.md](references/writing.md) when writing.

## Find the owner

Read the repository's agent instructions and relevant existing specs, API contracts, code and tests. Identify whether this is a behavior change, an implementation bug against an existing rule, or documentation drift. Code shows implementation, not proof of intended policy. Never invent intent or alternatives.

Use `openspec/specs/<capability>/spec.md` for new durable behavior owners. During migration, existing domain docs or OpenSpec specs remain authoritative until explicitly replaced. Update the existing owner rather than creating a second copy. Link its actual relative path. Do not bulk-convert documents unless requested.

OpenAPI owns HTTP field shapes; schemas own database structure; specs explain observable business behavior. Architecture overviews and operational runbooks remain in their existing docs. Do not duplicate those contracts.

## Choose the smallest workflow

- Formatting, comments, or mechanical changes: no spec artifact.
- A bug that restores an already specified rule: use the existing spec and focused regression evidence; no new proposal unless scope or ambiguity requires it.
- A small supported behavior change: a short proposal and affected delta spec.
- Cross-repository contracts, migration, permission, concurrency, or substantial design: proposal, delta specs, design and tasks with applicable failure, compatibility and rollback checks.
- Durable technical choice with no behavior delta: proposal and design; do not fabricate requirements.

These are company defaults, not claims about the built-in OpenSpec schema. If the repository uses the OpenSpec CLI, inspect its actual version, configuration, status and artifact instructions and honor its required artifacts. Prefer a supported custom schema for lightweight modes; never silently omit required files, overwrite config, or install a CLI without need. Without the CLI, use Markdown templates and report that only manual structure/content review was performed, not OpenSpec validation.

Read only the needed templates under `assets/`. Use stable capability names, not PR numbers or temporary implementation names. Preserve `Purpose`, `Requirements`, `Requirement:` and `Scenario:` headings for OpenSpec compatibility; use Korean prose.

## Implement and reconcile

Keep proposed changes under `openspec/changes/<change-name>/` separate from current specs. Describe added, modified or removed requirements as deltas, with full requirement text for modifications. Changes may evolve as implementation reveals constraints.

For each affected behavior, compare the agreed requirement, real runtime path and decisive test or manual evidence. Scenarios are acceptance criteria, not proof of execution; checked task boxes and document validation are not runtime evidence. Do not mechanically add tests for every document edit.

For cross-repository work, name one owner for each rule and link consumer-specific specs. Verify each affected repository independently. Do not claim a whole flow complete from one repository's tests.

Before updating current specs, review the resulting delta against verified implementation and authorized policy. Do not publish proposed or partially implemented behavior as current. Report code verification and deployment verification separately; a branch spec does not prove production deployment.

On completion, merge the supported deltas into current specs and archive the corresponding change under `openspec/changes/archive/YYYY-MM-DD-<change-name>/` using the repository's supported workflow. Link enduring design rationale from the current spec to the archived design instead of creating a duplicate ADR. Preserve existing decisions and source links during migration. Do not archive required unfinished work as completed; a cancelled change must remain clearly cancelled and must not update current behavior.

When another change has modified the same requirement, reread and reconcile rather than overwriting it. Existing commit, merge, deployment and human approval boundaries still apply.

## Company memory

Repository specs remain the detailed owner. If Company Brain is connected and authorized, use company-work-log for a shareable summary, stable document links, verified outcomes and remaining work. Exclude credentials, personal data and sensitive company information. Do not upload raw transcripts or private design documents, and do not require memory access to maintain local specs.
