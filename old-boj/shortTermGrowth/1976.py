from collections import deque

def bfs(adj, start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        node = q.popleft()

        for idx, item in enumerate(adj[node]):
            if item and visit[idx] == 0:
                visit[idx] = 1
                q.append(idx)

n = int(input())
m = int(input())

adj = []
visit = [0] * n
for _ in range(n):
    adj.append(list(map(int, input().split())))
city = list(map(int,input().split()))
start = city[0] - 1

bfs(adj, start, visit)
flag = True
for item in city:
    if visit[item-1] == 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')