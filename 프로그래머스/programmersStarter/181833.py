# 특별한 이차원 배열1
def solution(n):
    answer = [[]]
    for i in range(n):
        if i + 1 < n: answer.append([])
        for j in range(n):
            answer[i] += [int(j == i)]
    return answer

# Best solution
def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n): answer[i][i] = 1
    return answer