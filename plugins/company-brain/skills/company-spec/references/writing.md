# Writing rules

- Write Korean prose with English technical identifiers and OpenSpec headings.
- Lead with the capability's observable purpose, then independently verifiable requirements.
- State actors, triggering conditions, results and meaningful denial/failure cases.
- Use SHALL/MUST for required behavior. Use SHOULD only when a supported exception is intentional.
- Use GIVEN/WHEN/THEN when conditions clarify the scenario; do not enumerate equivalent data variants.
- Keep technical choices, actual alternatives and accepted tradeoffs in design, not behavior requirements.
- Ask only for material intent absent from authoritative sources; never invent a reason from the diff.
- Keep current specs free of execution logs, local paths, exact run timings, one-run hashes and commit inventories.
- PR descriptions own change-scoped verification and readiness; CI owns raw logs; archived design owns historical rationale.
- Include only stable, relevant code/test and contract links. Links support the spec but do not replace a clear requirement.
- Keep one owner for each rule. Consumer documents describe their own observable behavior and link the owner.
- Remove unused template sections. Templates are starting points, not mandatory document quotas.

## Migration boundary

Existing specs and domain documents remain the owner until a deliberate migration compares their supported rules with requirements, code and tests. Record disagreements instead of declaring code or old docs automatically correct. Preserve confirmed rationale and supersession links. Update references before retiring a duplicate owner; no mass deletion or automatic conversion.
