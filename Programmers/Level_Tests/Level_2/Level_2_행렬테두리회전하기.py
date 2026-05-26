"""
***로직***
1. 입력 변수
- rows: 행을 담은 입력 변수
- cols: 열을 담은 입력 변수
- queries: 회전시킬 범위를 담은 배열
2. 핵심 변수
- matrix: 1부터 열x행까지 숫자를 담은 행렬
- temp: 덮어지기 전 미리 빼놓은 수
- min_value: 회전범위 안의 최솟값
- answer: 회전범위의 최솟값들을 담은 배열
3. 핵심 로직
step1: 행렬 생성
- 바깥 루프를 행(i) 기준으로, 안쪽 루프를 열(j) 기준으로 하여 (i-1)*cols + j 의 수를 열 갯수만큼 생성하여 행 갯수만큼 생성
step2: 회전 시키기
- queries 안에 회전시킬 행,열 좌표들을 인덱스에 넣기 쉽도록 새로운 변수에 대입
- 덮어 씌워지기 전 숫자를 미리 temp 변수에 복사, 그 수를 최솟값을 결정하는 변수에 대입
- 좌측 -> 하 -> 우측 -> 상 순으로 돌면서 값들을 당기고 최솟값을 비교하여 기존값보다 작으면 갱신
step3: 최솟값 출력
- 각 회전마다 최솟값을 answer 배열에 대입
- 미리 빼놓은 수를 matrix에 대입
4. 예외 처리
- 1번 인덱스 문제 방지: 입력되는 좌표(queries)는 1부터 시작하지만, 파이썬 배열은 0부터 시작하므로 모든 좌표값에 -1을 해 주어 인덱스 범위 초과(IndexError)를 예외 처리함
- 값 유실 예외 처리: 회전 시 첫 번째로 덮어씌워져 사라지는 좌측 상단 값을 미리 'temp' 변수에 대피시켜 데이터 유실 예외를 방지함
"""
def solution(rows, cols, queries):
    answer = []
    matrix = [[(i-1)*cols + j for j in range(1,cols+1)] for i in range(1,rows+1)]
    
    for x1,y1,x2,y2 in queries:
        r1,c1,r2,c2 = x1-1,y1-1,x2-1,y2-1
        
        # 좌측위 값 하나 복사
        temp = matrix[r1][c1]
        min_value = temp
        
        # 좌측변 값 당김
        for i in range(r1,r2):
            matrix[i][c1] = matrix[i+1][c1]
            min_value = min(matrix[i][c1],min_value)
        
        # 아래변 값 당김
        for i in range(c1,c2):
            matrix[r2][i] = matrix[r2][i+1]
            min_value = min(matrix[r2][i],min_value)
            
        # 우측변 값 당김
        for i in range(r2,r1,-1):
            matrix[i][c2] = matrix[i-1][c2]
            min_value = min(matrix[i][c2],min_value)
        
        # 윗변 값 당김
        for i in range(c2,c1,-1):
            matrix[r1][i] = matrix[r1][i-1]
            min_value = min(matrix[r1][i],min_value)
        
        answer.append(min_value)
        matrix[r1][c1+1] = temp
    
    return answer