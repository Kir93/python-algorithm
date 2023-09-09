from sys import stdin
input = stdin.readline

n = int(input()) + 1
ls = [[0]*1001 for _ in range(1001)]

for p in range(1, n):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            ls[i][j] = p

r = [0] * n

for i in range(1001):
    for j in range(1001):
        if ls[i][j]: r[ls[i][j]] += 1

for i in range(1, n):
    print(r[i])