"""Context reminder only: no transcript, credential, network or memory writes."""
import json
import sys


def reminder(event):
    if event.get('hook_event_name') != 'SessionStart':
        return {}
    return {'hookSpecificOutput': {'hookEventName': 'SessionStart', 'additionalContext':
        '명확한 회사 업무에서는 먼저 company-skills 관리 스킬로 회사 목록을 동기화하세요. '
        '최신 운영 지침은 company-brain 스킬의 고정 /company-brain/instructions 주소에서 확인하세요. '
        '명확한 Unboxers 회사 업무에서는 company-brain 스킬을 적용해 관련 회사 기억을 조회하고 '
        '중요한 변경 및 검증된 완료 결과를 답변 전에 company source에 기록하세요. '
        '매번 저장 직전에 전 직원에게 공식 공유 가능한지 확인하세요. 개인·애매한 업무, 민감한 회사 정보와 그 사실을 유추할 수 있는 요약, 원본 대화는 제외하고 불분명하면 저장을 생략하세요. '
        '실제 업무 결과를 저장한 뒤 같은 기록을 재조회하세요. 연결 테스트만으로 업무 기록 적용 완료라고 보고하지 마세요.'}}


if __name__ == '__main__':
    try:
        result = reminder(json.load(sys.stdin))
    except (ValueError, TypeError, AttributeError):
        result = {}
    print(json.dumps(result, ensure_ascii=False))
