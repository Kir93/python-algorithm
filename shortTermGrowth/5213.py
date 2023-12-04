from collections import deque
import sys


input = sys.stdin.readline
dx1 = [-1, 0, 1, 1, 0, -1]
dy1 = [1, 1, 1, 0, -1, 0]
dx2 = [-1, 0, 1, 1, 0, -1]
dy2 = [0, 1, 0, -1, -1, -1]


def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        if x % 2 == 1:
            dx, dy = dx1, dy1
        else:
            dx, dy = dx2, dy2
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if c[nx][ny] == 0:
                    if i <= 2:
                        if a[x][y][1] == a[nx][ny][0]:
                            c[nx][ny] = c[x][y] + 1
                            dir[nx][ny] = [x, y]
                            q.append([nx, ny])
                    else:
                        if a[x][y][0] == a[nx][ny][1]:
                            c[nx][ny] = c[x][y] + 1
                            dir[nx][ny] = [x, y]
                            q.append([nx, ny])


n = int(input())
a = [[[[] for _ in range(2)] for _ in range(n)] for _ in range(n)]
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            x, y = map(int, input().split())
            a[i][j] = [x, y]
    else:
        for j in range(n-1):
            x, y = map(int, input().split())
            a[i][j] = [x, y]

label = [[[] for _ in range(n)] for _ in range(n)]
num = 0
for i in range(n):
    for j in range(n):
        if i % 2 == 1 and j == n-1:
            continue
        num += 1
        label[i][j] = num

q = deque()
c = [[0]*n for _ in range(n)]
dir = [[[] for _ in range(n)] for _ in range(n)]
bfs(0, 0)

flag, ans = 0, []
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if c[i][j]:
            print(c[i][j])
            ans.append(label[i][j])
            x, y = i, j
            while x > 0 or y > 0:
                nx, ny = dir[x][y]
                ans.append(label[nx][ny])
                x, y = nx, ny
            flag = 1
            break
    if flag:
        break
ans.reverse()
for s in ans:
    print(s, end=' ')