import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int,input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res*10+t
        x=x//10
    return res

def isPrime(x):
    if x== 1: return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True


for x in data:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

#new mycode

import sys
#sys.stdin = open('input.txt', 'rt')


def isPrime(x):
    newN = ''
    for i in range(1, len(x)+1):
        newN += x[-i]
    newN = int(newN)
    if(newN == 1):
        return False
    for j in range(2, newN):
        if(newN % j == 0):
            return False
    return newN


n = int(input())
data = list(input().split())
for x in data:
    r = isPrime(x)
    if(r != False):
        print(r, end=' ')
