from math import gcd
int(input())
ls = list(map(int, input().split()))
for i in range(1, len(ls)):
    g = gcd(ls[0], ls[i])
    print(f'{ls[0]//g}/{ls[i]//g}')