n, k = map(int, input().split())
r = [True] * (n + 1)
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if r[j] != False: 
            r[j] = False
            k -= 1
            if k == 0: exit(print(j))