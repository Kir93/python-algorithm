def solution(t, p):
    answer = 0
    len_p = len(p)
    
    for i in range(len(t) - len_p + 1):
        check = t[i:len_p + i]
        if int(check) <= int(p):
            answer += 1
            
    return answer