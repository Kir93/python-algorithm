def solution(t, p):
    answer = 0
    
    for i in range(len(t)):
        check = t[i:len(p) + i]
        if len(check) < len(p):
            break
        if int(check) <= int(p):
            answer += 1
            
    return answer