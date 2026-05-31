def solution(wallet, bill):
    answer = 0
    
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        if min(wallet) < min(bill):
            answer += 1
            bill[bill.index(max(bill))] //= 2
        if max(wallet) < max(bill):
            answer += 1
            bill[bill.index(max(bill))] //= 2
        
    return answer