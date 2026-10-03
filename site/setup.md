# Company Skills 설치

직원 페이지: https://unboxerscorp.github.io/company-skills/

Company Skills 스킬 하나를 설치하고 사용하는 회사 작업마다 공용 목록을 확인한다. GitHub 계정은 필요 없다. 개인 스킬과 기존 인증·설정은 보존한다.

## Codex · Claude Code

1. https://unboxerscorp.github.io/company-skills/download/company-skills.zip 을 내려받고 company-skills 폴더를 Codex의 사용자 .agents/skills 또는 Claude Code의 사용자 .claude/skills에 설치한다. 같은 이름의 개인 설치가 있으면 덮어쓰지 않는다.
2. 설치된 SKILL.md를 읽고 포함된 scripts/sync.py를 해당 도구 옵션으로 실행한다. Python이 없으면 사용 가능한 설치 방법을 안내하고 직접 설치가 가능한 경우 진행한다. Git·Node는 필요 없다.
3. 새 스킬 추가, 수정, 관리하던 스킬 제거, 반복 실행 시 변경 없음이 확인된 항목만 보고한다. 새 채팅이 필요하면 안내한다.

## ChatGPT · Claude

앱이 제공하는 스킬·플러그인 설치 화면에서 Company Skills를 등록한다. Claude의 ZIP 업로드는 위 다운로드를 사용한다. ChatGPT에서 해당 설치 기능이 제공되지 않으면 SKILL.md를 읽어 현재 채팅에 적용하고 앱에서 가능한 지속 설정만 안내한다. 연결된 브라우저·데스크탑 조작 권한이 없으면 직접 필요한 단계만 설명한다. 설치·제거를 자동화할 수 없는 상태를 완료로 보고하지 않는다.

로컬 파일을 바꿀 수 없는 앱은 목록과 최신 SKILL.md를 작업마다 읽어 적용한다. 목록에서 빠진 업무 스킬은 적용하지 않는다. 실제 앱에 업로드된 개별 스킬 제거는 앱에서 조작이 필요할 수 있다.

## Grove

Grove 운영자가 이 절차를 요청한 실행 환경에만 적용한다. 실행 에이전트가 Codex 또는 Claude Code이면 해당 로컬 절차를 따른다. Company Brain 연결은 서비스 계정을 사용한다. 직원 개인 인증을 요구하지 않는다.

## Company Brain 연결

회사 기억 기능을 사용하려면 https://base-inbrain-develop.taile4260.ts.net/company-brain/setup 의 해당 앱 인증 절차를 따른다. 기존 연결이 정상이라면 재설정하지 않는다. 회사 Google 로그인과 필수 승인은 사용자가 진행한다. 전 직원에게 공식 공유 가능한 내용만 기록하며 민감 정보와 그 요약은 제외한다.

## 자동 반영의 범위

Company Skills 스킬을 사용할 때 동기화한다. 백그라운드 실행을 의미하지 않는다. 이 도구가 관리하지 않는 설치나 사용자가 수정한 파일은 보존한다. 목록·파일 검증이 실패하면 설치와 제거를 하지 않는다. 훅과 인증 설정은 자동 동기화 대상이 아니다.
