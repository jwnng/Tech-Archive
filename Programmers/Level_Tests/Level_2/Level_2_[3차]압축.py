"""
***로직***
1. 입력 변수:
    msg: 전체 문자열
2. 핵심 변수
    lzw_dict: 사전 색인 번호를 담은 딕셔너리
    start: 검사할 문자열의 시작 위치 인덱스
    end: 검사할 문자열의 끝 위치 인덱스
    w: 현재 입력
3. 핵심 로직
step1: 사전 초기화
- 알파벳 순서에 맞게 lzw_dict를 초기화
step2: 가장 긴 일치 단어 찾기 
- 현재 위치에서 시작하여 사전에 등록된 가장 긴 문자열 w를 찾는다
- 만약 w+c가 사전에 있다면 w를 w+c로 업데이트
step3: 출력 및 사전 등록
- w+c가 사전에 없다면 마지막 w의 색인 번호를 answer에 추가한다
- w+c를 사전에 새로 등록한다
- 입력 위치를 w의 길이만큼 이동시킨다
4. 예외 처리
- 문자열의 마지막 부분에 도달했을 때 다음 글자가 없다면 w의 색인 번호를 출력하고 종료한다
"""
def solution(msg):
    answer = []
    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    lzw_dict = { chr(i+64): i for i in range(1,27)} 
    
    
    start = 0
    while start < len(msg):
        w = msg[start] # 현재 입력 기본 한 글자
        end = start + 1
    
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        while end < len(msg) and w + msg[end] in lzw_dict:
            w += msg[end]
            end += 1
    
        # 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
        answer.append(lzw_dict[w])
        
        # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if end < len(msg):
            lzw_dict[w + msg[end]] = len(lzw_dict)+1
        
        # 5. 단계 2로 돌아간다.
        start = end
        
    return answer