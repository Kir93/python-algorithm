def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    
    for i in range(0, len(score), m):
        box = score[i:m + i]
        if len(box) < m: break
        answer += min(box) * m
        
    return answer