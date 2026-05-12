"""
***로직***
1. 입력 변수
- record: 채팅방의 활동 로그
2. 핵심 변수
- us_db: 유저 아이디: 닉네임 값을 딕셔너리로 저장
- actions: 출력해야 할 메시지들을 저장한 배열
3. 핵심 로직
step1: 유저 정보 최신화 및 로그 수집
- 전체 레코드를 순회하며 데이터를 분리한다.
- 명령어가 Enter나 Change일 경우 딕셔너리에 닉네임을 덮어쓴다
- 명령어가 Enter나 Leave일 경우 actions 배열에 (유저id,명령어) 튜플로 저장한다
step2: 최종 메시지 생성
- actions 배열을 순회하며 명령어가 Enter이라면 answer 배열에 입장 메시지를 저장
- Leave이라면 answer 배열에 퇴장 메시지를 저장
4. 예외처리
인덱스 에러 방지:
- Leave 명령어는 닉네임 데이터를 포함하지 않으므로, 명령어를 먼저 확인하여 인덱스에 접근한다
"""
# 기존 채팅방의 메시지 닉네임도 전부 변경, 중복 허용
from collections import defaultdict
def solution(record):
    answer = []
    us_db = defaultdict(str)
    actions = []
    
    for curr in record:
        curr = curr.split()
        command = curr[0]
        usid = curr[1]
        
            
        if command in ['Enter','Change']:
            name = curr[2]
            us_db[usid] = name
            
        if command in ['Enter','Leave']:
            actions.append((usid,command))
            
    # 최종 메세지 출력
    for usid,command in actions:
        if command == 'Enter':
            answer.append(f"{us_db[usid]}님이 들어왔습니다.")
        else:
            answer.append(f"{us_db[usid]}님이 나갔습니다.")
            
    return answer