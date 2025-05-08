import sys
n=int(input())
w=int(input())
s = []
dp = [[-1]*(w+1) for _ in range(w+1)]
for _ in range(w):
    p,q = map(int,input().split())
    s.append((p,q))
s1=[(1,1)]+s
s2=[(n,n)]+s

def f(p1,p2,n,w):
    if p1==w or p2==w:
        return 0
    if dp[p1][p2]!=-1:
        return dp[p1][p2]
    x=s1[p1][0]
    y=s1[p1][1]
    a=s2[p2][0]
    b=s2[p2][1]
    nxt=max(p1,p2)+1
    l1=abs(s[nxt-1][0]-x)+abs(s[nxt-1][1]-y)
    l2=abs(s[nxt-1][0]-a)+abs(s[nxt-1][1]-b)
    dp[p1][p2] = min(l1+f(nxt,p2,n,w),l2+f(p1,nxt,n,w))
    return dp[p1][p2]

def path(p1,p2,w):
    if p1==w or p2==w:
        return
    x=s1[p1][0]
    y=s1[p1][1]
    a=s2[p2][0]
    b=s2[p2][1]
    nxt=max(p1,p2)+1
    l1=abs(s[nxt-1][0]-x)+abs(s[nxt-1][1]-y)
    l2=abs(s[nxt-1][0]-a)+abs(s[nxt-1][1]-b)
    if l1+dp[nxt][p2] < l2+dp[p1][nxt]:
        print(1)
        path(nxt,p2,w)
    else:
        print(2)
        path(p1,nxt,w)
print(f(0,0,n,w))
path(0,0,w)