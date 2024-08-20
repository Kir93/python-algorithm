import sys
from collections import deque
input = sys.stdin.readline

q = deque()
N = int(input())
friend = [[] for _ in range(N+1)]
while True:
	a, b = map(int,input().split())
	if a == -1:
		break
	else:
		friend[a].append(b)
		friend[b].append(a)
 
# bfs함수
def bfs(n):
	visited[n] = True
	q.append(n)
	while q:
		x = q.popleft()
		for i in friend[x]:
			if not visited[i]:
				q.append(i)
				dist[i] = dist[x] + 1
				visited[i] = True
 
chairman = []
dab = 51
for i in range(1, N+1):
	dist = [0] * (N+1)
	visited = [False] * (N+1)
	bfs(i)
	m = max(dist)
	if m == dab:
		chairman.append(i)
	elif m < dab:
		chairman = [i]
		dab = m
 
print(dab, len(chairman))
print(*chairman)