# 피자 나눠 먹기 (2)
from math import gcd

def solution(n):
    return n*6 // gcd(n, 6) // 6

# gcd 직접 구현
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def solution(n):
    return n*6 // gcd(n, 6) // 6