from math import log2, ceil
import sys

si = sys.stdin.readline

M = int(si())
arr = [int(si()) for _ in range(M)]

N = max(arr)
m = 1 << ceil(log2(N)) + 1
A = [1] * N + [0] * (m - N)
A[0] = A[1] = 0
A[2] = 1

p = 469762049


def fft(a, inverse):
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
    step = 2
    while step <= n:
        half = step // 2
        u = pow(3, p // step, p)
        if inverse:
            u = pow(u, p - 2, p)
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j + half] = (a[j] - v) % p
                a[j] = (a[j] + v) % p
                w = (u * w) % p
        step *= 2

    if inverse:
        num = p - (p - 1) // n
        for i in range(n):
            a[i] = (a[i] * num) % p


for _ in range(4, N, 2):
    A[_] = 0

for i in range(3, N, 2):
    if A[i] == 0:
        continue
    A[i] = 1
    for j in range(i + i, N, i):
        A[j] = 0

B = [0] * m
B[4] = 1
for _ in range(3, N // 2, 2):
    if A[_]:
        B[2 * _] = 1

fft(A, 0)
fft(B, 0)
T = [A[i] * B[i] for i in range(m)]
fft(T, 1)

ans = [0] * M
for _ in range(M):
    ans[_] = T[arr[_]]
print('\n'.join(map(str, ans)))