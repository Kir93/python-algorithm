# 특별한 이차원 배열 2
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]: return 0
    else: return 1

# Best solution - 최악의 경우 시간 복잡도는 동일하지만 평균 적으로 절반으로 줄어듬
def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][j] != arr[j][i]: return 0
    return 1