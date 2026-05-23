"""
***로직***
1. 입력 변수
- N: 스테이지 수
- stages: 사람들이 도달해있는 스테이지 배열
2. 핵심 변수
- fail: 스테이지마다 머물러있는 플레이어 수를 담은 딕셔너리
- Lv: [스테이지 번호, 실패율] 쌍을 담은 배열을 담은 배열
- total: 스테이지마다 클리어하거나, 도달해있는 사람의 수 
3. 핵심 로직
step1: 스테이지마다 플레이어 수 체크
- collections 라이브러리에서 Counter함수 임포트
- stages를 카운터함수로 스테이지번호: 플레이어 수 생성 형태의 해시 맵(딕셔너리) 생성
step2: 실패율 체크
- 실패율을 구할 때 분모가 될 전체 플레이어 수 변수 생성
- 1부터 N+1까지 돌면서 인원수가 0이 아니라면 Lv= [스테이지 번호, 실패율] 쌍을 담은 배열 형태로 append
- 현재 스테이지 인원수는 (전체 인원수 - 이전단계 클리어 수) 요소가 변할 때마다 갱신
- 인원수가 0이라면 [idx,0] 형태로 append
step3: 정렬 및 정답 추출
- 람다 함수를 이용하여 첫번째는 실패율이 높은걸 기준으로, 두번째는 번호가 낮은걸 기준으로 정렬
- 리스트 컴프리헨션을 이용하여 Lv의 첫번째 요소만 추출
4. 예외 처리
- 도달한 플레이어 수가 0명이라면 실패율을 0으로 바로 대입
"""
from collections import Counter
def solution(N, stages):
    fail = Counter(stages)
    
    Lv = []
    total = len(stages)
    for i in range(1,N+1):
        if total == 0:
            Lv.append([i,0])
        else:   
            Lv.append([i,fail[i]/total])
        total -= fail[i]
    
    Lv = sorted(Lv,key=lambda x: (x[1],-x[0]),reverse=True)
    return list(x[0] for x in Lv)