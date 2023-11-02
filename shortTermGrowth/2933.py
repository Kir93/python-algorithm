from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def destroy(i, left):
    i, j = r - i, 0
    if left == 1:
        for k in range(c):
            if a[i][k] == 'x':
                a[i][k] = '.'
                j = k
                break
    else:
        for k in range(c-1, -1, -1):
            if a[i][k] == 'x':
                a[i][k] = '.'
                j = k
                break

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < r and 0 <= nj < c:
            if a[ni][nj] == 'x':
                dq.append([ni, nj])

def bfs(x, y):
    q = deque()
    check = [[0]*c for _ in range(r)]
    fall_list = []
    q.append([x, y])
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == r-1:
            return
        if a[x+1][y] == '.':
            fall_list.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] == 'x' and not check[nx][ny]:
                    check[nx][ny] = 1
                    q.append([nx, ny])

    fall(check, fall_list)

def fall(check, fall_list):
    k, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + k == r-1:
                flag = 1
                break
            if a[i+k+1][j] == 'x' and not check[i+k+1][j]:
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(r-2, -1, -1):
        for j in range(c):
            if a[i][j] == 'x' and check[i][j]:
                a[i][j] = '.'
                a[i+k][j] = 'x'

r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
n = int(input())
s = list(map(int, input().split()))
dq = deque()

left = 1
while n:
    index = s.pop(0)
    destroy(index, left)

    while dq:
        x, y = dq.popleft()
        bfs(x, y)

    left *= -1
    n -= 1

for i in range(r):
    for j in range(c):
        print(a[i][j], end='')
    print()