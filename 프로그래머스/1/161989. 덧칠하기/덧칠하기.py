def solution(n, m, section):
    answer = 0
    i = 0
    
    for s in section:
        if s > i:
            answer += 1
            i = s + m - 1
            
    return answer