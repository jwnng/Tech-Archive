import math
def solution(n):
    # return sum([i for i in range(1,n+1) if n % i == 0])
    answer = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            answer.append(i)
            if i != n // i:
                answer.append(n//i)

    return sum(answer)
            
print(solution(12))