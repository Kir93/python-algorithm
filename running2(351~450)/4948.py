from math import sqrt
from sys import stdin

input = stdin.readline

def isPrime(num):
    if num < 2: return False
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0: return False
    return True

while True:
    n = int(input())
    r = 0
    if n == 0: exit()
    else:
        for i in range(n+1, 2*n + 1):
            if isPrime(i): r += 1
        print(r)