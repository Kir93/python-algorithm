import sys
from math import ceil,log2
input=sys.stdin.readline
def plus(start,end,left,right,node,diff):
    if right<start or left>end:
        return
    if left<=start and end<=right:
        tree[node]+=diff
        return
    mid=(start+end)//2
    plus(start,mid,left,right,2*node,diff)
    plus(mid+1,end,left,right,2*node+1,diff)

def find(node):
    global ans
    while node>=1:
        ans+=tree[node]
        node//=2


n=int(input())
size=2**ceil(log2(n))
tree=[0]*(2*size)
for i,j in enumerate(list(map(int,input().split()))):
    tree[size+i]=j
m=int(input())
for i in range(m):
    query=list(map(int,input().split()))
    if query[0]==1:
        plus(1,size,query[1],query[2],1,query[3])
    else:
        ans=0
        find(size+query[1]-1)
        print(ans)