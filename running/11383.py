n, m = map(int, input().split())
r = 'Eyfa'
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]
for i in range(len(a)):
    ca = ''
    for x in a[i]:
        ca += x*2
    if ca != b[i]:
        r = 'Not Eyfa'
        break
print(r)