import sys
input=sys.stdin.readline

INF=10000000001

I=(-INF, -INF, -INF, 0)#lmx, rmx, mx, sum

def merge(a, b):
    almx, armx, amx, asum=a
    blmx, brmx, bmx, bsum=b
    ret=(max(almx, asum+blmx), max(brmx, armx+bsum), max(amx, bmx, armx+blmx), asum+bsum)
    return ret

def init(tree, arr):
    n=len(arr)
    tree[n:]=arr
    for i in range(n-1, 0, -1):
        tree[i]=merge(tree[i<<1], tree[i<<1|1])
        
def query(tree, l, r):
    n=len(tree)>>1
    l+=n-1;r+=n-1
    lret=rret=I
    while l<=r:
        if l&1:
            lret=merge(lret, tree[l])
            l+=1
        if r&1^1:
            rret=merge(tree[r], rret)
            r-=1
        l>>=1;r>>=1
    return merge(lret, rret)

n=int(input())
A=[*map(lambda x:(int(x),)*4, input().split())]
M=int(input())

seg=[(0,)*4 for _ in range(n<<1)]

init(seg, A)

for _ in range(M):
    i, j=map(int, input().split())
    print(query(seg, i, j)[2])