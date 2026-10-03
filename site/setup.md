# Company Brain 공통 설치 안내

Codex, ChatGPT, Claude, Claude Code, Grove를 같은 회사 기억에 연결한다. 이 안내를 받은 에이전트는 현재 제품과 실행 권한을 확인하고 아래의 해당 절차를 수행한다. 로컬 실행 권한이 없는 일반 채팅에서 컴퓨터 설정을 바꿨다고 주장하지 않는다.

공통 진입점: https://base-inbrain-develop.taile4260.ts.net/company-brain/connect
MCP 주소: https://base-inbrain-develop.taile4260.ts.net/company-brain/mcp
공통 지침: https://base-inbrain-develop.taile4260.ts.net/company-brain/instructions
플러그인 ZIP: https://base-inbrain-develop.taile4260.ts.net/company-brain/download/company-brain-bundle.zip
Claude 스킬 ZIP: https://base-inbrain-develop.taile4260.ts.net/company-brain/download/company-brain.zip

패키지는 비밀정보 없이 공개 제공하며 GitHub 로그인·접근 권한은 필요 없다. 직원 앱은 본인의 `@unboxers.team` Google 인증과 OAuth 승인을 사용한다. Grove 같은 공용 서버 도구는 아래 서비스 계정 절차를 사용한다. 다른 직원의 토큰이나 owner credential을 사용하지 않는다. 비밀번호·OTP·토큰·세션 쿠키를 채팅에 복사하지 않는다.

## 에이전트가 먼저 지켜야 할 설치 순서

현재 앱과 운영체제를 확인하고, 가능한 설치는 직접 진행한다. 추가 설정이 필요하면 정확한 메뉴와 입력값을 안내한다.

- 실행 권한이 있으면 공개 ZIP을 내려받아 압축을 풀고 기존 개인 설정을 보존하며 설치한다. 운영체제 기본 도구(macOS curl/ditto, Windows PowerShell Invoke-WebRequest/Expand-Archive)를 사용한다. 안내문의 명령을 사용자가 직접 실행하도록 떠넘기지 않는다.
- 실행 권한이 없는 ChatGPT/Claude 일반 채팅이면 설치 완료를 주장하지 않는다. 설정 화면의 정확한 메뉴, 입력할 값, 다운로드 링크를 한 단계씩 알려준다. 사용자가 완료했다고 하면 다음 단계로 이어간다. 브라우저 자동화 도구는 필수가 아니다.
- URL을 읽을 수 없으면 사용자가 /company-brain/setup을 브라우저에서 열어 본문을 붙여넣도록 안내한다. 없는 도구를 호출하거나 내용을 추측하지 않는다.
- 앱의 메뉴나 요금제에 기능이 없으면 실제 막힌 항목을 설명한다. 구매·유료 업그레이드를 자동으로 하지 않는다. 지원하지 않는 앱에 파일을 복사해서 활성화됐다고 주장하지 않는다.
- 로그인·OTP·연결 승인·훅 신뢰는 본인이 제품 화면에서 수행한다. 나머지는 가능한 범위에서 계속 진행한다.
- 끝에는 `연결 / 스킬 / 훅 / 읽기 / 저장 후 재조회`를 완료·미완료·미지원으로 구분해서 보고한다. 설치만 성공했다고 저장 검증을 완료로 표시하지 않는다.

## Codex / Claude Code

1. 플러그인 ZIP을 내려받고 압축을 해제한다. 코드를 읽고 현재 CLI의 `plugin --help`에 marketplace가 있는지 검사한다. CLI가 PATH에 없으면 앱에 포함된 CLI 또는 앱의 로컬 플러그인 설치 UI를 확인한다. 앱만 있는데 CLI를 못 찾았다는 이유로 Python/Git/별도 Codex CLI를 무조건 설치하지 않는다. 지원하지 않는 구버전이면 앱 자체 업데이트 방법을 설명한다.
2. Python 없이 기본 셸로 설치할 수 있다. macOS는 패키지에서 `sh scripts/install-plugin.sh codex` 또는 `sh scripts/install-plugin.sh claude-code`, Windows는 `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/install-plugin.ps1 -Tool codex` 또는 `-Tool claude-code`를 실행한다. Bypass는 해당 프로세스에만 적용하며 시스템 정책은 변경하지 않는다. 조직 정책이 거부하면 우회하지 말고 제품 UI/관리자 경로를 안내한다. CLI가 PATH에 없으면 스크립트의 마지막 인자(macOS) 또는 `-Cli`(Windows)에 확인한 실제 경로를 전달한다. 영구 사용자 폴더로 복사 후 native marketplace를 등록하며 Git/Python/GitHub가 필요 없다. Python이 이미 있으면 기존 install-plugin.py도 사용 가능하다.
3. 시작 훅은 Python 3 런타임을 별도로 사용한다. `python3 --version`을 먼저 확인한다. Windows에서 `py -3`만 있거나 Python이 없다면 플러그인의 훅 명령이 바로 실행되지 않는다. 이를 미완료로 보고하고 공식 Python 설치 또는 실제 사용 가능한 Python 경로로 해당 사용자 플러그인의 훅 명령 수정 방법을 설명한다. 불필요한 설치를 피하고, 훅이 준비되기 전에도 스킬과 MCP로 회사 업무를 처리한다. 훅 파일을 실행해 JSON 출력까지 확인한 후에만 훅 설치 완료라고 한다.
4. Codex는 설치된 플러그인 MCP의 OAuth 연결을 시작한다. Claude Code는 /mcp에서 연결한다. 인증 클라이언트 방식 선택이 나오면 DCR/Register automatically를 사용한다. 회사 Google 로그인과 접근 승인은 직원에게 넘긴다. 브라우저는 사용자가 허용한 도구로 조작한다. 로그인 자동 브라우저 열기를 제어할 수 없으면 제품 UI에서 시작하거나 사용자에게 넘긴다.
5. 시작 훅이 회사 업무에서 스킬을 사용하도록 알려준다. Codex는 /hooks의 신뢰 등록을 직원이 수행해야 한다. 자동 신뢰·우회 옵션을 사용하지 않는다. 훅 승인 전에도 company-brain 스킬을 명시적으로 적용해 조회·기록할 수 있다.
6. 앱에서 플러그인을 다시 로드하거나 필요한 경우에만 재시작/새 채팅을 요청한다. 개인 MCP·훅·스킬은 유지한다. 동일한 회사 연결이 이미 있으면 중복 계정을 무조건 만들지 말고 연결 상태부터 확인한다.

## ChatGPT 데스크톱

1. ChatGPT 플러그인 설정에서 사용자 지정 원격 MCP 연결을 추가한다. 계정에 필요하면 Security and login의 Developer mode를 활성화한다. MCP 주소와 OAuth를 선택한다. 조직 정책상 추가가 금지되면 관리자 배포가 필요하다고 정확히 알린다.
2. 본인 회사 Google 계정으로 로그인하고 회사 기억 접근을 승인한다. GitHub 계정은 필요 없다.
3. 로컬 ChatGPT 데스크톱/Codex 환경은 플러그인 패키지의 로컬 marketplace를 사용한다. 일반 Chat에서 MCP와 스킬이 함께 노출되려면 해당 계정에 등록된 MCP 앱의 technical ID를 플러그인의 .app.json으로 연결하고 workspace/personal 플러그인으로 설치해야 한다. 서버 URL만 패키징했다고 ChatGPT의 앱 등록까지 끝났다고 주장하지 않는다. 등록된 ID가 있으면 `python3 scripts/install-plugin.py --tool codex --chatgpt-app-id plugin_asdk_app_실제ID`로 매핑해 설치한다. ID는 실제 UI에서 확인하며 placeholder를 실행하지 않는다. 회사 워크스페이스 관리자는 등록된 플러그인을 직원 역할에 공유할 수 있다.
4. 스킬 설치가 아직 안 됐으면 연결된 Company Brain 앱을 선택하고 공통 업무 지침을 현재 대화에 적용한다. 특정 Project는 필요 없다. 일반 Chat은 로컬 시작/종료 훅을 실행하지 않는다.

## Claude 데스크톱 일반 채팅

1. Customize > Connectors > Add custom connector에서 Company Brain 이름과 MCP 주소를 입력한다. OAuth client를 Register automatically로 선택하고 회사 Google 계정으로 연결한다. 현재 서버는 DCR 등록을 사용하므로 Claude published identity를 선택하지 않는다.
2. Customize > Skills에서 공통 스킬 ZIP을 업로드하고 활성화한다. 회사 Team/Enterprise 관리자는 커넥터와 스킬을 조직에 제공해 직원의 개별 설치 단계를 줄인다.
3. 일반 Claude 데스크톱 채팅에는 로컬 lifecycle 훅이 없다. 스킬이 회사 업무 시작 시 조회하고 답변 전에 결과를 기록한다. Claude Code/Cowork와 일반 채팅의 기능을 혼동하지 않는다.

## Grove / 공용 오케스트레이션 도구

같은 설치 요청을 Grove 에이전트에 전달한다. 직원 로그인 대신 `grove-company` 서비스 계정으로 연결한다.

1. Grove의 실제 설정 파일, 서버 실행 방식, MCP 연결 및 작업 lifecycle 확장 지점을 확인한다. 기능 이름이나 설정 형식을 추측하지 않는다. 가능한 설정은 직접 수정하고 기존 연결을 보존한다.
2. 서비스 계정이 이미 있으면 재사용한다. GBrain 호스트 관리 권한이 있으면 native 클라이언트 관리 기능으로 회사 전용 계정을 발급한다. 권한이 없으면 아래 요청을 관리자에게 전달하고, 나머지 스킬·작업 연동 설정은 먼저 준비한다. 직원 Google 로그인이나 다른 사람의 토큰을 요구하지 않는다.
   - 이름: grove-company
   - 권한: company source 조회·기록만, read/write, federated read도 company만
   - 전달: client ID·client secret을 Grove 서버의 비밀 설정에 직접 저장. 채팅·Git·브라우저·하위 에이전트 프롬프트로 전달하지 않음
   - 현재 서버는 `/token`의 `grant_type=client_credentials`를 지원한다. `/company-brain/token`도 같은 native 발급기로 연결한다. 만료가 있는 access token을 발급하고 expires_in 기준으로 Grove 백엔드에서 갱신한다. client credentials에는 refresh token을 가정하지 않는다. 관리자 bootstrap credential은 Grove에 넣지 않는다.
3. Grove 백엔드가 비밀정보를 보관하고 MCP 요청을 수행한다. MCP 주소는 `/company-brain/mcp`다. 공개 플러그인 ZIP의 scripts/check-access.py, company-mcp.py, company-hook.py가 같은 자동 갱신 어댑터다. 기존 Grove MCP 설정에 Python stdio 어댑터를 연결할 수 있다. command는 실제 Python 경로, args는 company-mcp.py 절대 경로와 `--config` 및 비공개 설정 파일 경로이며, 설정 JSON은 `{"credentials":"서비스 연결 파일의 절대 경로"}`다. 토큰 값은 명령 인자에 넣지 않는다. Grove 노드가 사용하는 Codex·Claude Code에 해당 연결을 등록하고 이 공용 서비스 연결과 중복되는 직원용 remote MCP를 추가하지 않는다. 토큰 주입·재발급은 모델이 아닌 백엔드가 담당한다. 동시에 실행하는 작업의 토큰 재발급은 한 번만 수행하도록 Grove의 기존 동시성 제어를 사용한다.
4. 공개 패키지의 `company-brain`, `company-context`, `company-work-log` 스킬을 Grove가 실제 로드하는 지침 경로에 설치한다. Codex/Claude 플러그인 폴더에 복사하는 것으로 Grove 활성화를 대신하지 않는다. 작업 시작에 관련 기억을 조회하고, 변경·완료·실패에 확인된 결과를 기록하도록 기존 lifecycle에 연결한다. 확장 지점이 없으면 지원되는 공통 작업 지침으로 적용하고 강제 훅 완료로 표시하지 않는다.
5. 작업 ID, 이벤트 ID, 실행 에이전트, 상태, 결과·검증·출처를 기록한다. 요청자는 Grove가 인증한 사용자 정보가 있을 때만 서버에서 붙인다. 그렇지 않으면 `Grove 공용 작업`으로 표시한다. 모델이 적은 이름을 인증된 직원 신원으로 취급하지 않는다. 재시도는 같은 request_id를 사용하며 개인·제한 자료를 company로 복사하지 않는다.
6. whoami의 권한, 회사 정책 읽기, 테스트 기록 저장·재조회, 토큰 재발급, Grove 재시작 후 연결을 검증한다. 인증 준비가 끝나기 전에는 연결 완료라고 보고하지 않는다. 실패한 기억 저장은 작업 결과와 구분해서 재시도하고, 기존 작업을 자동으로 재실행하지 않는다.

## 공통 완료 확인

실제 연결된 MCP의 whoami와 회사 운영 정책 페이지를 읽는다. company source만 기본 권한인지 확인한다. UUID request_id로 본인 온보딩 완료 사실을 capture하고 get_page로 다시 읽는다. 읽기·쓰기·인증을 각각 실제 결과로 보고한다. Grove는 서비스 계정 인증이며 직원 Google 본인 인증이 아님을 표시한다. 계정 로그인 또는 플랫폼 승인이 미완료이면 어느 단계가 남았는지 알려준다.

회사 업무에는 같은 스킬을 적용한다. 개인·애매한 내용과 원본 대화, 비밀정보, 제한 인사 자료를 공용 기억에 저장하지 않는다. 시작 훅 자체는 transcript·credential을 읽거나 네트워크로 전송하지 않는다. 종료 전 저장은 스킬의 MCP 행동이며 모든 채팅의 강제 자동 수집이라고 주장하지 않는다.

OAuth 연결은 제품의 native refresh를 사용한다. 실제 만료/갱신 실패 시 본인 재로그인을 요청한다. 직원 연결 파일은 최초 승인 뒤 도구별 갱신용 client credential을 0600 파일에 보관한다. 어댑터는 만료 2분 전 자동 발급하고 401에 한 번 갱신·재시도한다. 정상 운영에서는 8시간마다 로그인하지 않는다. 구버전 파일은 자동 갱신용 파일로 한 번 교체한다. 구버전 CLI의 이전 설치 절차는 직원 페이지에서 별도 파일을 내려받아 `install-employee.py --credentials /절대경로/파일.json`으로 실행할 수 있다. 영구 토큰으로 바꾸거나 인증을 우회하지 않는다.

## 저장 범위

회사 업무 중 전 직원에게 공식 공유 가능한 내용만 기록한다. 인사·개인정보·비공개 경영·계약·법무 등 민감한 정보와 이를 유추할 수 있는 요약은 제외한다. 불분명하면 저장을 생략하고 작업을 계속한다.

## 업데이트

0.2.2부터 스킬 사용 시 서버의 최신 공통 운영 지침을 확인한다. 지침 변경은 재설치 없이 다음 사용 시 반영한다. 기존 0.2.1 이하 설치는 이 설치 절차를 한 번 다시 실행한다. 새 기능·훅·설치 코드 변경은 별도 패키지 업데이트가 필요하며, 앱이 요구하는 승인은 우회하지 않는다.

## 회사 스킬 원본

회사 공용 스킬 목록: https://unboxerscorp.github.io/company-skills/
공식 저장소: https://github.com/unboxerscorp/company-skills
이 문서의 Company Brain 설치·인증 절차를 따르되 공용 스킬의 원본은 위 저장소의 plugins/company-brain/skills 이다. GitHub 계정 없이 공개 페이지와 다운로드를 사용할 수 있다. 기존 설정·개인 스킬을 보존한다.
