import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
reverse = [[] for _ in range(n + 1)]
cash = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    reverse[b].append(a)

for i in range(1, n + 1):
    cash[i] = int(sys.stdin.readline())

s, p = map(int, sys.stdin.readline().split())
restaurant = list(map(int, sys.stdin.readline().split()))

stack = []
visit = [0] * (n + 1)
for i in range(1, n + 1):
    if not visit[i]:
        visit[i] = 1
        queue = [i]
        while queue:
            cur = queue[-1]
            for nxt in graph[cur]:
                if not visit[nxt]:
                    visit[nxt] = 1
                    queue.append(nxt)
                    break
            else:
                stack.append(queue.pop())

scc = []
scc_idx = [-1] * (n + 1)
finish = [0] * (n + 1)
while stack:
    node = stack.pop()
    if not finish[node]:
        finish[node] = 1
        res = []
        queue = [node]
        while queue:
            cur = queue[-1]
            for nxt in reverse[cur]:
                if not finish[nxt]:
                    finish[nxt] = 1
                    queue.append(nxt)
                    break
            else:
                top = queue.pop()
                scc_idx[top] = len(scc)
                res.append(top)

        scc.append(res)

money = [0] * len(scc)
for i in range(1, n + 1):
    if scc_idx[i] != -1:
        money[scc_idx[i]] += cash[i]

indegree = [0] * len(scc)
visit = [0] * (n + 1)
visit[s] = 1
queue = [s]
while queue:
    i = queue.pop()
    for j in graph[i]:
        if scc_idx[i] != scc_idx[j]:
            indegree[scc_idx[j]] += 1
        if not visit[j]:
            visit[j] = 1
            queue.append(j)

ans = [0] * len(scc)
ans[scc_idx[s]] = money[scc_idx[s]]
queue = [scc_idx[s]]
while queue:
    cur_idx = queue.pop()
    for i in scc[cur_idx]:
        for j in graph[i]:
            if cur_idx != scc_idx[j]:
                ans[scc_idx[j]] = max(ans[scc_idx[j]], ans[cur_idx] + money[scc_idx[j]])
                indegree[scc_idx[j]] -= 1
                if indegree[scc_idx[j]] == 0:
                    queue.append(scc_idx[j])

sol = 0
for i in restaurant:
    if scc_idx[i] != -1:
        sol = max(sol, ans[scc_idx[i]])
print(sol)