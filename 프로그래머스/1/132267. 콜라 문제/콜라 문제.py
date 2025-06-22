def solution(a, b, n):
    answer = 0
    
    while n//a > 0:
        r = (n//a) * b
        answer += r
        n = r + n%a
        
    return answer