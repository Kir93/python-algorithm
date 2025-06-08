def solution(s):
    answer = []
    r = {}
    
    for i in range(len(s)):
        if s[i] in r: answer.append(i - r[s[i]])
        else: answer.append(-1)
        r[s[i]] = i
        
    return answer