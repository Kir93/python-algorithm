import sys
input = sys.stdin.readline
mod = 998244353
g = 3

def ntt(a, inverse):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j: a[i], a[j] = a[j], a[i]
    step = 2
    while step <= n:
        half = step//2
        u = pow(g, (mod-1)//step, mod)
        if inverse: u = pow(u, -1, mod)
        for i in range(0, n, step):
            w = 1
            for j in range(i, i+half):
                tmp = a[j + half]*w % mod
                a[j+half] = (a[j] - tmp) % mod
                a[j] = (a[j] + tmp) % mod
                w = w * u % mod
        step *= 2
    if inverse:
        inv = pow(n, -1, mod)
        for i in range(n):
            a[i] = a[i] * inv % mod

def multiply(a, b):
    deg = len(a) + len(b) - 1
    n = 1 << deg.bit_length()
    a.extend([0 for _ in range(n-len(a))])
    b.extend([0 for _ in range(n-len(b))])
    ntt(a, False)
    ntt(b, False)
    for i in range(n):
        a[i] = a[i] * b[i] % mod
    ntt(a, True)
    return a[:deg]

nu = int(input())
arr1 = [*map(int, input().split())]
p1 = [0 for _ in range(60001)]
for i in arr1:
    p1[i+30000] = 1
nm = int(input())
arr2 = [*map(int, input().split())]
p2 = [0 for _ in range(120001)]
for i in arr2:
    p2[2*i+60000] = 1
ni = int(input())
arr3 = [*map(int, input().split())]
p3 = [0 for _ in range(60001)]
for i in arr3:
    p3[i+30000] = 1
p4 = multiply(p1, p3)
ans = 0
for i in range(120001):
    if p2[i]:
        ans += p4[i]
print(ans)