# Unboxers Company Skills

직원용 공용 AI 스킬: https://unboxerscorp.github.io/company-skills/

## 관리

`plugins/company-brain/skills/`가 Company Brain 세 스킬의 원본이다. 공통 플러그인도 이 저장소에서 관리한다. 새 스킬은 해당 플러그인의 skills 디렉터리에 추가하고 직원 페이지의 목록을 함께 갱신한다.

서버·OAuth·Company Brain 데이터·기존 설치 패키지는 [company-brain](https://github.com/unboxerscorp/company-brain)에서 관리한다. 그 저장소에는 이 원본의 고정 커밋 스냅샷을 배포 호환용으로 유지한다. 두 곳에서 따로 수정하지 않는다.

## 배포

main 변경 시 GitHub Actions가 직원 페이지와 Claude 스킬 ZIP을 GitHub Pages에 배포한다. 로컬 확인: `python3 scripts/build-site.py`. 공개 사이트에는 업무 기록이나 인증정보를 넣지 않는다.

Codex·Claude Code용 Git 기반 플러그인 마켓플레이스와 직원용 웹 설치 안내를 제공한다. 앱별 승인·훅 신뢰 절차는 유지한다. 기존 버전은 한 번 업데이트해야 최신 운영 지침 조회가 적용된다.
