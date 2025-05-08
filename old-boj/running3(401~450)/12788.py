int(input())
m, n = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
pen = m * n
r = 0
for p in a:
    if pen > 0:
        r += 1
        pen -= p
    else: break
print('STRESS' if pen > 0 else r)