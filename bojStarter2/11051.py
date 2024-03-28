import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print((result // divisor) % 10007)