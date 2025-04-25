import sys
from cmath import exp,pi
def fft(a):
    N=len(a)
    if N==1:
        return a
    a_even=fft(a[0::2])
    a_odd=fft(a[1::2])
    w_N=[exp(2j*pi*n/N) for n in range(N//2)]
    return [a_even[n] +w_N[n]*a_odd[n] for n in range(N//2)] + [a_even[n]-w_N[n]*a_odd[n] for n in range(N//2)]
 
def ifft(a):
    N=len(a)
    if N==1:
        return a
    a_even=ifft(a[0::2])
    a_odd=ifft(a[1::2])
    w_N=[exp(-2j*pi*n/N) for n in range(N//2)]
    return [a_even[n] +w_N[n]*a_odd[n] for n in range(N//2)] + [a_even[n]-w_N[n]*a_odd[n] for n in range(N//2)]
 
M=int(sys.stdin.readline())
N=2*M
even=0
for i in range(18):
    if M==2**i:
        even=-100
        break
    elif N<2**i:
        even=i
        break
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
if even==-100:
    A=A[:]+A[:]
    B=B[-1::-1]+[0]*M
    C=[0]*N
    A_fft=fft(A)
    B_fft=fft(B)
    for i in range(N):
        C[i]=A_fft[i]*B_fft[i]
 
    C_ifft=ifft(C)
    for k in range(N):
        C_ifft[k]=round(C_ifft[k].real/N)
    max_number=max(C_ifft)
else:
    N_prime=2**i
    N,N_prime=N_prime,N
    A=A[:]+[0]*(N-N_prime//2)
    B=B[-1::-1]+[0]*(N-N_prime)+B[-1::-1]
 
    C=[0]*N
    A_fft=fft(A)
    B_fft=fft(B)
    for i in range(N):
        C[i]=A_fft[i]*B_fft[i]
    C_ifft=ifft(C)
    for k in range(N):
        C_ifft[k]=round(C_ifft[k].real/N)
    max_number=max(C_ifft)
print(max_number)