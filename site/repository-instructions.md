# 회사 저장소 공통 지침

회사 저장소의 공통 지침 파일에 아래 블록을 추가합니다. Codex와 Claude가 같은 파일을 읽도록 AGENTS.md 또는 CLAUDE.md에서 연결하고 기존 지침은 보존합니다. 스킬 본문을 저장소에 복사하지 않습니다.

## Company Skills

For explicitly identified Unboxers company work, start with `company-skills`: https://unboxerscorp.github.io/company-skills/skills/company-skills/SKILL.md. Follow its supported synchronization workflow to check the current catalog and apply only skills relevant to the task. Keep shared skill bodies and templates in company-skills, not in this repository.

Retrieve relevant company context when Company Brain is connected. Use `company-spec` for product/workflow behavior and durable specification changes, and `company-work-log` to save shareable actions and verified outcomes, then read the saved record back. Exclude personal, ambiguous and sensitive content. Do not collect past chats without explicit authorization.

Preserve repository-specific document ownership, testing, commit and deployment rules; shared skills do not grant additional permissions. If catalog synchronization or Company Brain is unavailable, continue authorized repository work with verified local guidance, report the limitation, and never claim synchronization or recording succeeded. Skip company-memory writes when the latest sharing policy cannot be verified.
