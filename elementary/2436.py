import sys

input = sys.stdin.readline
from math import sqrt

g, l = map(int, input().split())

divide = l // g 

def gcd(a, b):
    if a % b == 0:
        return b 

    return gcd(b, a % b)

for a in range(int(sqrt(divide)), 0, -1): 
    b = int(divide / a) 

    if divide % a == 0 and gcd(a, b) == 1: 
        print(a * g, b * g)
        break