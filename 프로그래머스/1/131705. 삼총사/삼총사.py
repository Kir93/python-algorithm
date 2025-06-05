from itertools import combinations

def solution(number):
    answer = 0
    
    for combi in combinations(number, 3):
        if sum(combi) == 0:
            answer += 1
    
    return answer