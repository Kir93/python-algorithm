n, m = map(int, input().split())
ls = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for z in range(i-1, j):
        ls[z] = k
print(*ls)