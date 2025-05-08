n, m = map(int, input().split())
r = []
for i in range(n):
    p, l = map(int, input().split())
    mi = list(map(int, input().split()))
    mi.sort(reverse=True)
    if p < l: r.append(1)
    else: r.append(mi[l-1])
r.sort()
cnt = 0
for i in r:
    m -= i
    cnt += 1
    if m < 0:
        print(cnt - 1)
        break
if m > 0: print(cnt)