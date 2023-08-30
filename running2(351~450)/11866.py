n, k = map(int, input().split())

idx = 0
q = [i for i in range(1, n+1)]
res = []
while q:
    idx += k - 1
    if idx >= len(q): idx %= len(q)
    res.append(str(q.pop(idx)))
print(f'<{", ".join(res)}>')