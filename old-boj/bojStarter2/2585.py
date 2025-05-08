import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def cal_dist(n1,n2):
    distance = ((coordinate[n1][0] - coordinate[n2][0])**2 + (coordinate[n1][1] - coordinate[n2][1])**2)**(1/2)
    return int((distance // 10) + 1 if distance % 10 else (distance // 10))

def check(limit):
    visited = set([0])
    q = deque([(0,0)])
    while q:
        w, cnt = q.popleft()
        if dist[w][n+1] <= limit:
            return True
        if cnt >= k: continue
        for nxt in range(n+2):
            if nxt not in visited and dist[w][nxt] <= limit:
                visited.add(nxt)
                q.append((nxt,cnt+1))
    return False

n, k = map(int, input().split())
coordinate = [(0,0)] + [tuple(map(int,input().split())) for _ in range(n)] + [(10000,10000)]
dist = [[0] * (n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        dist[i][j] = cal_dist(i,j)

left, right = 0, cal_dist(0,n+1)
result = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)