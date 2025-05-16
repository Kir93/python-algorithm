import sys
input = sys.stdin.readline

def update(L,R,T,S,i,v):
    unit = len(L)//2
    pos = unit+i
    L[pos] = R[pos] = T[pos] = S[pos] = L[pos]+v
    
    while pos > 1:
        left,right = 0,0
        if pos%2 == 0:
            left,right = pos,pos+1
        else:
            left,right = pos-1,pos
        par = pos//2
        L[par] = max(L[left],S[left]+L[right])
        R[par] = max(R[right],S[right]+R[left])
        T[par] = max(T[left],T[right],R[left]+L[right])
        S[par] = S[left]+S[right]
        pos = par

N = int(input())
X = []
Y = []
P = [[0,0,0] for _ in range(N)]

for i in range(N):
    x,y,w = map(int,input().split())
    X.append((x,i))
    Y.append((y,i))
    P[i][2] = w

X.sort()
Y.sort()

c = 0

for i in range(N):
    x,idx = X[i]
    P[idx][0] = c
    if i < N-1 and X[i+1][0] != x:
        c += 1
        
c = 0

for i in range(N):
    y,idx = Y[i]
    P[idx][1] = c
    if i < N-1 and Y[i+1][0] != y:
        c += 1
        
c += 1
ytox = [set() for _ in range(c)]

for x,y,w in P:
    ytox[y].add((x,w))

maxv = 0
unit = 1

while unit < N: unit *= 2

for i in range(c):
    L = [0]*(2*unit)
    R = [0]*(2*unit)
    T = [0]*(2*unit)
    S = [0]*(2*unit)
    for j in range(i,c):
        for x,w in ytox[j]:
            update(L,R,T,S,x,w)
        if T[1] > maxv:
            maxv = T[1]

print(maxv)