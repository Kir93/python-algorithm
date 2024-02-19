import sys
from math import gcd

N = int(sys.stdin.readline())

a = int(sys.stdin.readline())

arr = []

for i in range(N-1):
    num = int(sys.stdin.readline())
    arr.append(num - a)
    a = num

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

result = 0
for each in arr:
    result += each // g - 1
print(result)