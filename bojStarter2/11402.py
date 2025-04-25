import math
N,K,p=map(int,input().split());s=1
while N+K:s*=math.comb(N%p,K%p);N//=p;K//=p
print(s%p)