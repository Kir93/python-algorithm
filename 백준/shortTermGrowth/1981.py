from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if left <= a[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
    return 0

n = int(input())

a, r_max, l_min = [], 0, sys.maxsize
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    l_min = min(l_min, min(row))
    r_max = max(r_max, max(row))

l_max = min(a[0][0], a[n-1][n-1])
r_min = max(a[0][0], a[n-1][n-1])

left, right = l_min, r_min
ans = sys.maxsize
while l_min <= left <= l_max and r_min <= right <= r_max:
    l_flag, r_flag = 0, 0
    if bfs():
        ans = min(ans, right - left)
        left += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            left += 1
            right += 1
        else:
            right += 1
            r_flag = 1
print(ans)