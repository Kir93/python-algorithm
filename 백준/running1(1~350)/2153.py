from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x) + 1)):
        if x%i == 0: return False
    return True

n = list(input())
r = 0

for x in n:
    if x.isupper(): r += ord(x) - 38
    else: r += ord(x) - 96
    
if isPrime(r): print('It is a prime word.')
else: print('It is not a prime word.')