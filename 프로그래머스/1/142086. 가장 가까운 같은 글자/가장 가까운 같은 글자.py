def solution(s):
    answer = []
    r = {}
    for i in range(len(s)):
        if s[i] in r.keys():
            answer.append(i - r[s[i]])
            r.update({s[i]: i})
        else:
            answer.append(-1)
            r.setdefault(s[i], i)
        
    return answer