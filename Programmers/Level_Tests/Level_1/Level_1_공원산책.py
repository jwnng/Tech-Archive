"""
***로직***
step1: 위치 읽기
- park를 순회하면 시작 지점 인덱스 저장 후 반복문 break
step2: 명령 수행
- routes를 순회하며 조건에 맞지 않으면 continue로 넘김 맞다면 r,c 갱신
step3: 정답 출력
"""
def solution(park, routes):
    answer = []
    r,c = 0,0
    H,W = len(park), len(park[0])
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                r,c = i,j
                break
                
    move = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    
    for dir in routes:
        op, n = dir.split()
        n = int(n)
        
        dr,dc = move[op]
        nr,nc = r + dr*n, c + dc*n
        
        if 0 <= nr < H and 0 <= nc < W:
            if any(park[r + dr*i][c + dc*i] == 'X' for i in range(1,n+1)):
                continue
            
            r,c = nr,nc
        
    return [r,c]