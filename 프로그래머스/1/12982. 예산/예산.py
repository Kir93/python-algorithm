def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if budget - x >= 0:
            budget -= x
            answer += 1
        else: break
        
    return answer