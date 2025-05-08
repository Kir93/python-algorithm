from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    r = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            x = (i**2 + j**2 + m)%(i*j)
            if x == 0: r += 1
    print(r)