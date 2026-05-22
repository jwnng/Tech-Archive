"""
***로직***
1. 입력 변수
- numbers: 눌려야 할 번호를 담은 배열
- hand: 손잡이를 나타내는 변수
2. 핵심 변수
- num_loc: 키패드 번호와 위치 순서쌍을 담은 딕셔너리
- L_loc, R_loc: 누른 뒤의 손의 위치
- distance: 키패드 위치 차를 계산하는 함수
- answer: 정답을 출력하는 문자열
3. 핵심 로직
step1: 키패드와 손 위치 생성
- 키패드의 번호와 위치를 키:(위치 쌍) 형태를 담은 딕셔너리 생성
- 딕셔너리를 기준으로 왼손과 오른손의 첫번째 위치 대입
step2: 거리 계산
- 거리를 계산하는 함수를 만들고 파이썬 라이브러리에 내장된 abs함수를 이용하여 멘해튼 거리 공식을 활용하여 두 좌표의 절댓값 차이 합을 리턴
step3: 키패드 누르기
- 눌러야 할 번호 배열을 순회하며 왼쪽, 오른쪽, 가운데로 눌러야 할 번호를 조건문으로 나눔
- 가운데 키패드를 누를 때 왼손 위치| 오른손 위치 중 어느 곳이 가까운지에 따라 결정
- 거리가 같을 때 어느 손잡이인지에 따라 결정
4. 예외 처리
- 키패드 생성 시 배열로 생성할 경우 인덱스를 꺼내서 쓰지 못하는 이유로 딕셔너리로 생성
"""
def solution(numbers, hand):
    answer = ''
    num_loc = {
        1:(0,0), 2: (0,1), 3:(0,2),
        4:(1,0), 5: (1,1), 6:(1,2),
        7:(2,0), 8: (2,1), 9:(2,2),
        '*':(3,0), 0: (3,1), '#':(3,2)
    }
    L_loc = num_loc['*']
    R_loc = num_loc['#']
    
    def distance(pos1,pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            L_loc = num_loc[n]
        elif n in [3,6,9]:
            answer += 'R'
            R_loc = num_loc[n]
        else:
            if distance(num_loc[n],L_loc) > distance(num_loc[n],R_loc):
                answer += 'R'
                R_loc = num_loc[n]
            elif distance(num_loc[n],L_loc) < distance(num_loc[n],R_loc):
                answer += 'L'
                L_loc = num_loc[n]
            else:
                if hand == 'right':
                    answer += 'R'
                    R_loc = num_loc[n]
                else:
                    answer += 'L'
                    L_loc = num_loc[n]
            
    return answer