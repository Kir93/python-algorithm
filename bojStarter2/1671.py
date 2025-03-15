import sys
input = sys.stdin.readline

n = int(input())

shark = [list(map(int, input().split())) for _ in range(n)]
target = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            target[i].append(j)
        elif shark[i][0] <= shark[j][0] and shark[i][1] <= shark[j][1] and shark[i][2] <= shark[j][2]:
            target[j].append(i)

def dfs(x):
    for i in target[x]:
        if checked[i]:
            continue
        checked[i] = True
        if visited[i] == -1 or dfs(visited[i]):
            visited[i] = x
            return True
    return False

res = 0
for i in range(n):
    checked = [False for _ in range(n)]
    if dfs(i):
        res += 1
    checked = [False for _ in range(n)]
    if dfs(i):
        res += 1

print(n-res)