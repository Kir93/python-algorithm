# from math import gcd, lcm
def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)
def lcm(a, b):
    return a*b//gcd(a,b)
x, y = map(int, input().split())
print(gcd(x, y))
print(lcm(x, y))