from math import gcd
x, y = map(int, input().split())
print('1'*gcd(x, y))