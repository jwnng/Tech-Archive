"""
***로직***
1. 입력 변수
- participant: 참가자들이 있는 배열
- completion: 완주자들이 있는 배열
2. 핵심 변수
- hash_map: 참가자와 완주자를 관리하는 해시 테이블
3. 핵심 로직
step1: 참가자 리스트 생성
- collections 라이브러리 defaultdict 모듈을 임포트해서 hash_map 기본값이 정수인 해시를 생성
step2: 참가자와 완주자 배열 순회, 추가 및 제거
- 먼저 참가자 배열을 순회하며 해시에 정수값을 1씩 증가시킴
- 그 다음 완주자 배열을 순회하며 해시에서 정수값 -1을 함
step3: 완주하지 못한 자 출력
- 해시를 돌며 완주하지 못한 자는 해시 값이 1이기 때문에 value가 1이상이면 key값을 리턴
4. 예외 처리
- 참가자 수가 최대 100,000이기 때문에 이중 중첩문 사용시 O(n^2)의 시간복잡도를 갖기 때문에 시간초과 발생
- 먼저 참가자 수 - 완주자 수가 1이 아니면 오류 발생
- 동명이인이 있을 수 있기 때문에 해시의 value값을 1씩 증가시키는 로직 사용
"""
# 재풀이
from collections import defaultdict
def solution(participant, completion):
    hash_map = defaultdict(int)
    
    if len(participant) - len(completion) != 1:
        return False
    for p in participant:
        hash_map[p] += 1
        
    for c in completion:
        hash_map[c] -= 1
        
    answer = []
    for k,v in hash_map.items():
        if v >= 1:
            return k
            
"""        
def sollution(participant,completion):
    hash = {}

    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1

    for c in completion:
            hash[c] -= 1

    for key in hash:
        if hash[key] > 0:
            return key
"""
"""
from collections import Counter

def sollution(participant,completion):
    return hash_map((Counter(participant) - Counter(completion)).keys())[0]
"""

"""
import collections

def sollution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return hash_map(answer.key())[0]
"""