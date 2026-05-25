"""
***로직***
1. 입력 변수
2. 핵심 변수
3. 핵심 로직
4. 예외 처리
"""
def solution(rows, columns, queries):
    answer = []
    M = [[(j * columns + i) for i in range(1, columns + 1)] for j in range(rows)]
    
    for line in queries:
        x1,y1,x2,y2 = line
        # print(x1,y1,x2,y2)
        temp1 = M[x1-1][y1-1] # 왼쪽 위
        temp2 = M[x2-1][y1-1] # 왼쪽 아래
        temp3 = M[x1-1][y2-1] # 오른쪽 위
        temp4 = M[x2-1][y1-1] # 오른쪽 아래
        # 위쪽
        for i in range(y1,y2):
            M[x1-1][i] = M[x1-1][i-1]
        # 아래쪽
        for i in range(y2-1,y1,-1):
            M[x2-1][i] = M[x1-1][i-1]
        #오른쪽
        M[x2][y2-1]= temp3
        for i in range(x1+1,x2):
            M[i][y2-1] = M[i-1][y2-1]
        #왼쪽
        M[x2-2][y1-1] = temp2
        for i in range(x2-2,x1,-1):
            M[i][y1-1] = M[i-1][y1-1]
        
        
        
        
    return answer