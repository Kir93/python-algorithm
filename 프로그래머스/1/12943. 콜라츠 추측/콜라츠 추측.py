def solution(num):
    answer = 0
    while num != 1:
        if answer >= 500:
            answer = -1
            break
            
        if num%2 == 0: num //= 2
        elif num%2 != 0: num = num * 3 + 1
        
        answer += 1
        
    return answer