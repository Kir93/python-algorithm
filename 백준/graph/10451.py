def solution(v):
    visited[v] = 1
    next = arr[v]
    if visited[next] == 0:
        solution(next)
    return

t = int(input())
arr = [0]
for _ in range(t):
    cnt = 0
    n = int(input())
    visited = [0] * (n + 1)
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    for i in range(1, n + 1):
        if visited[i] == 0:
            solution(i)
            cnt += 1
    print(cnt)