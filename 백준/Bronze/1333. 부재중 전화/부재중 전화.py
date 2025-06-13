n, l, d = map(int, input().split())
t = n * l + (n - 1) * 5
s = [False] * t
for i in range(0, t, l + 5):
    for j in range(i, i + l):
        s[j] = True
for i in range( 0, t, d):
    if not s[i]:
        print(i)
        break
else:
    print(i + d)