# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    ls = [0 for _ in range(len(included))]
    
    for i in range(len(included)):
        r = a if i == 0 else ls[i-1] + d 
        ls[i] = r
        if included[i] == True: answer += r
        
    return answer

# Best Solution
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer