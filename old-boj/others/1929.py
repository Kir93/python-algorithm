# 제곱근을 이용하자 int(x**0.5) or sqrt함수 이용
# 근사 제곱근 구한 뒤 그 값으로 계산하면 시간초과 안 나옴
from math import sqrt
def isPrime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0: return False
    return True
m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1: continue
    if isPrime(i): print(i)