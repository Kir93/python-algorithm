def getsfxarr(s):
    n = len(s)
    t = 1
    sfxarr = list(range(n))
    group = [s[i] for i in range(n)] + [-1]
    newgroup = [0 for _ in range(n + 1)]
    newgroup[sfxarr[0]] = 0
    newgroup[n] = -1
    
    while t < n:
        sfxarr.sort(key = lambda x: (group[x], group[min(x+t, n)]))
        for i in range(1, n):
            p, q = sfxarr[i-1], sfxarr[i]
            if group[p] != group[q] or group[min(p + t, n)] != group[min(q + t, n)]:
                newgroup[q] = newgroup[p] + 1
            else:
                newgroup[q] = newgroup[p]
        group = newgroup[:]
        t <<= 1
    return sfxarr

n, k = map(int, input().split())
arr = list(reversed(list(map(int, input().split()))))
cnt = 1
sfxarr = getsfxarr(arr + arr)
for i in range(len(sfxarr)):
    if sfxarr[i] < n and sfxarr[i] > 0:
        if cnt == k:
            k = sfxarr[i]
            break
        else:
            cnt += 1
ans = list(arr[k:]) + list(arr[:k])
print(' '.join(str(i) for i in ans))