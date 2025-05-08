from math import gcd
int(input())
ls = list(map(int, input().split()))
g = gcd(ls[0], gcd(ls[1], ls[-1]))
for i in range(1, (g//2)+1):
    if g%i == 0: print(i)
print(g)