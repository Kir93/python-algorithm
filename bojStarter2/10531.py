import sys; input = sys.stdin.readline
from cmath import exp, pi
from math import ceil, log2

# 거듭제곱을 이용한 FFT
def fft(a, inv):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    p = (-2 if inv else 2) * pi
    s = 2
    while s <= n:
        z = exp(complex(0, p / s))
        for i in range(0, n, s):
            w = 1 + 0j
            for j in range(i, i + (s >> 1)):
                tmp = a[j + (s >> 1)] * w
                a[j + (s >> 1)] = a[j] - tmp
                a[j] += tmp
                w *= z
        s <<= 1
    return [x / n for x in a] if inv else a

N = 1 << ceil(log2(400002)) # 합성곱을 구할 두 다항식의 길이 합(200001 * 2)보다 큰, 가장 작은 2의 거듭제곱
A = [0] * N

# 가능한 거리는 1
A[0] = 1
for _ in range(int(input())):
    A[int(input())] = 1

# 2타 이내에 가능한 모든 거리를 구해야 하므로
# 가능한 거리의 리스트인 A와 자기 자신인 A의 합성곱을 구해야 한다.
A = fft(A, False)
for i in range(N):
    A[i] *= A[i]
A = fft(A, True)

# M개의 구멍마다 가능한지 확인
# 만약 가능한 거리라면 실수 부분이 0보다 크다.
answer = 0
for _ in range(int(input())):
    i = int(input())
    if round(A[i].real):
        print(i, round(A[i].real))
        answer += 1
print(answer)