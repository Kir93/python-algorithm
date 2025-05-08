n, m = map(int, input().split())
r = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    r[a] += 1
    r[b] += 1
for i in range(1, n+1): print(r[i])