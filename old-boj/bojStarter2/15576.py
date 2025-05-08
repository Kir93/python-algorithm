import sys;
from cmath import exp, pi
from math import ceil, log2
input = sys.stdin.readline

# 거듭제곱을 이용한 FFT
def fft(A, inv = False):
    n = len(A)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            A[i], A[j] = A[j], A[i]

    p = (-2 if inv else 2) * pi
    s = 2
    while s <= n:
        z = exp(complex(0, p / s))
        for i in range(0, n, s):
            w = 1 + 0j
            for j in range(i, i + (s >> 1)):
                tmp = A[j + (s >> 1)] * w
                A[j + (s >> 1)] = A[j] - tmp
                A[j] += tmp
                w *= z
        s <<= 1

    if inv:
        for i in range(n):
            A[i] /= n

A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))

a = len(A)
b = len(B)
N = 1 << ceil(log2(a + b - 1)) # 필요한 길이(a + b - 1)보다 크면서, 가장 작은 2의 거듭제곱

# 거듭제곱을 이용한 FFT를 위해 길이를 2의 거듭제곱이 되게끔 맞춘다.
A += [0] * (N - a)
B += [0] * (N - b)

# A와 B의 합성곱 구하기
fft(A); fft(B)
for i in range(N):
    A[i] *= B[i]
fft(A, True)

# a의 길이의 정수와 b의 길이의 정수의 곱은 최대 a + b다.
result = [0] * (a + b)
for i in range(a + b - 1):
    result[i + 1] = round(A[i].real)

# 올림 처리
for i in range(a + b - 1, 0, -1):
    result[i - 1] += result[i] // 10
    result[i] %= 10

if result[0]: # 첫 자리는 0일 수도 있다.
    print(result[0], end = '')
print(*result[1:], sep = '')