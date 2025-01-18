# 수열과 구간 쿼리 4 - 다시 풀기
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0: arr[i] += 1
    return arr