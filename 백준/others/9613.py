from math import gcd
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    r = 0
    for i in range(2, len(ls)):
        for j in range(1, i):
            r += gcd(ls[i],ls[j])
    print(r)