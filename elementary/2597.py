from sys import stdin
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    x, y = a[i]

    if x == y:
        continue
    
    m = (x + y) / 2
    n = max(m, n - m)

    for j in range(i + 1, 3):
        a[j] = [abs(m - a[j][0]), abs(m - a[j][1])]

print(n)
