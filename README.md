# Unboxers Company Skills

직원용 공용 AI 스킬: https://unboxerscorp.github.io/company-skills/

## 관리

`plugins/company-brain/skills/`가 회사 공용 스킬의 원본이다. 공통 플러그인도 이 저장소에서 관리한다. 새 스킬은 해당 플러그인의 skills 디렉터리에 추가하고 직원 페이지의 목록을 함께 갱신한다.

`company-spec`은 제품·업무 규칙과 설계 근거를 OpenSpec 방식으로 관리한다. 기존 문서의 정본을 먼저 찾고 변경 규모에 맞는 문서만 작성한다. 한국어 본문과 OpenSpec 구조를 사용하며, 템플릿은 스킬의 `assets/`에 있다. 기존 문서 일괄 변환과 OpenSpec CLI 설치는 자동 수행하지 않는다.

서버·OAuth·Company Brain 데이터·기존 설치 패키지는 [company-brain](https://github.com/unboxerscorp/company-brain)에서 관리한다. 그 저장소에는 이 원본의 고정 커밋 스냅샷을 배포 호환용으로 유지한다. 두 곳에서 따로 수정하지 않는다.

## 배포

main 변경 시 GitHub Actions가 직원 페이지와 Claude 스킬 ZIP을 GitHub Pages에 배포한다. 로컬 확인: `python3 scripts/build-site.py`. 공개 사이트에는 업무 기록이나 인증정보를 넣지 않는다.

Codex·Claude Code용 Git 기반 플러그인 마켓플레이스와 직원용 웹 설치 안내를 제공한다. 앱별 승인·훅 신뢰 절차는 유지한다. 기존 버전은 한 번 업데이트해야 최신 운영 지침 조회가 적용된다.

## Company Skills 관리 스킬

직원은 company-skills 하나를 설치한다. 회사 작업에 이 스킬을 적용할 때 공개 catalog.json과 SHA-256 파일 목록을 확인한다. Codex·Claude Code에서는 관리 중인 설치만 추가·갱신·제거하고 개인 설치와 로컬 수정은 보존한다. ChatGPT·Claude에서는 최신 지침을 읽어 적용하며 앱 설치 UI는 별도 조작이 필요할 수 있다. 자동 배경 실행이 아니다. 검증: python3 scripts/test-sync.py.

## 저장소 연결

모든 회사 저장소는 개별 스킬 대신 `company-skills`를 공통 진입점으로 연결한다. [공통 지침 블록](site/repository-instructions.md)을 기존 AGENTS.md·CLAUDE.md의 공유 지침에 추가하고 저장소 고유 규칙을 보존한다. 새 스킬과 변경·제거는 공용 카탈로그를 통해 반영한다.
