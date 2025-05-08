n = int(input())
perm = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if perm[i-1] > perm[i]:
        for j in range(n-1, 0, -1):
            if perm[i-1] > perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm = perm[:i] + sorted(perm[i:], reverse=True)
                exit(print(*perm))
print(-1)