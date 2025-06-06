def solution(s):
    r = s.split(' ')
    answer = ''
    for i in range(len(r)):
        for j in range(len(r[i])):
            answer += r[i][j].upper() if j%2 == 0 else r[i][j].lower()
        if len(r) != i + 1:
            answer += ' '
        
            
    return answer