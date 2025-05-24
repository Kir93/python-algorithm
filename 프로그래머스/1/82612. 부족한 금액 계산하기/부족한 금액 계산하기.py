def solution(price, money, count):
    answer = 0
    
    for i in range(1, count+1):
        answer += price * i
        
    return 0 if money >= answer else answer - money