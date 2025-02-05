# 구슬을 나누는 경우의 수 - retry
def fac(num):
    r = 1
    for i in range(1, num+1): r *= i
    return r

def solution(balls, share):
    n = fac(balls)
    m = fac(share)
    nm = fac(balls - share)
    
    return n / (nm * m)

# Best solution - math.factorial(팩토리얼) 사용
from math import factorial
def solution(balls, share):
    n = factorial(balls)
    m = factorial(share)
    nm = factorial(balls - share)
    
    return n / (nm * m)

# Best solution - math.comb(조합) 사용
from math import comb
def solution(balls, share):
    return comb(balls, share)