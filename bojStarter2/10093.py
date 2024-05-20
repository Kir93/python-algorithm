a, b = map(int, input().split())
minN = min(a, b)
maxN = max(a, b)
if minN == maxN or minN+1 == maxN: n = 0
else: n = maxN - minN - 1
print(n)

for i in range(minN+1, maxN): print(i, end=' ')