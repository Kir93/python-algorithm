import sys

input=sys.stdin.readline

n=int(input())

def translate(L):
    res=[0]*len(L)
    for i in range(len(L)):
        res[L[i]-1]=i+1
    return res
L1=translate(list(map(int,input().split())))
L2=translate(list(map(int,input().split())))
L3=translate(list(map(int,input().split())))

class sgTree:
    def __init__(self,L):
        self.len=len(L)
        self.tree=[10**10]*self.len+L
        for i in range(self.len-1, 0, -1):
            self.tree[i]=min(self.tree[2*i],self.tree[2*i+1])

    def update(self, i, val):
        i+=(self.len-1)
        self.tree[i]=val
        while i>1:
            i//=2
            self.tree[i]=min(self.tree[2*i],self.tree[2*i+1])

    def res(self, l, r):
        l+=(self.len-1)
        r+=(self.len-1)
        tot=10**10
        while l<=r:
            if l%2:
                tot=min(tot, self.tree[l])
                l+=1
            l//=2
            if not r%2:
                tot=min(tot, self.tree[r])
                r-=1
            r//=2
        return tot
    
score = []
for i in range(n):
    score.append((L1[i], L2[i], L3[i]))
score.sort()
L=[10**10]*(n)
s=sgTree(L)
res=0
for i in range(n):
    k=s.res(1, score[i][1])
    if k>score[i][2]:res+=1
    s.update(score[i][1], score[i][2])

print(res)