# 유한소수 판별하기 - retry

# 유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(a, b):
    n = b//gcd(a, b)
    while n > 1:
        if n%2 == 0:
            n //= 2
        elif n%5 == 0:
            n //= 5
        else: return 2
    return 1