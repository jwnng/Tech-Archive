"""
***로직***
1. 입력 변수:
- s: 괄호로 이루어진 문자열
2. 핵심 변수:
- answer: 괄호를 관리하는 스택
3. 핵심 로직:
step1: 문자열 확인
- 문자열이 비어있거나 첫번째 괄호가 올바르지 않다면 오류를 리턴
step2: 문자열 관리
- answer 스택을 생성하고 전체 문자열을 돌면서 '(' 괄호를 만나면 스택에 저장,
')'를 만나면 스택에서 빠지도록 관리
step3: 결과 출력
- 반복문을 다 돌고나서도 스택이 비어있지 않다면 오류 출력, 비어있다면 올바른 문자열
4. 예외 처리:
- 시작부터 잘못된 경우: 첫 글자가 ')'로 시작하면 올바른 괄호가 아니므로 False를 바리턴
- 닫는 괄호가 많은 경우: 반복문 도중 ')'를 만났으나 스택이 비어있다면 False를 리턴
- 여는 괄호가 많은 경우: 문자열을 모두 순회했음에도 스택에 요소가 남아았다면 올바르지 않은 괄호이므로 False 리턴
"""

# 재풀이
def solution(s):
    if not s or s[0] == ')':
        return False
    
    answer = []
    
    for c in s:
        if c == '(':
            answer.append(c)
        else:
            if answer:
                answer.pop()
            else:
                return False
            
    if answer:
        return False
    else:
        return True
    
        
"""def solution(s):
    answer = True
    S = []
    if s[0] == ')' or not s:
        return False
    
    for char in s:
        if char == '(':
            S.append(char)
        else:
            if len(S) == 0:
                return False
            else:
                S.pop()
        
    if len(S) == 0:
        return True
    else:
        return False

"""