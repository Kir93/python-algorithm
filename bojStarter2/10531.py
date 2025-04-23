import sys;
input=sys.stdin.readline
P=998244353

def fft(a, inverse=False):
    n = len(a)
    j = 0
    for i in range(1,n):
        reverse = n // 2
        while j >= reverse:
            j -= reverse
            reverse //= 2
        j += reverse
        if i < j:
            a[i], a[j] = a[j], a[i]
    step = 2
    while step <= n: 
        half = step // 2
        u = pow(3,P//step,P)
        if inverse:
            u = pow(u,P-2,P)
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j+half] = (a[j]-v)%P
                a[j] = (a[j]+v)%P
                w = (u*w)%P
        step *= 2

    if inverse:
        num = P-(P-1)//n
        for i in range(n):
            a[i] = (a[i]*num)%P

N=int(input())
x=[0]*(1<<19)
x[0]=1
for i in range(N):
    x[int(input())]+=1
fft(x)
for i in range(1<<19):
    x[i]**=2
    x[i]%=P
fft(x,1)
M=int(input())
s=0
for i in range(M):
    s+=x[int(input())]>0
print(s)