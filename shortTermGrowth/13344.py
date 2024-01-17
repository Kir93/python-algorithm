import sys
from collections import deque
input=sys.stdin.readline

def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]

def merge(a,b):
    q=find(a)
    w=find(b)
    if q==w:
        return
    else:
        if q<w:

            parent[w]=q
        else:
            parent[q]=w

n,m=map(int,input().split())
parent=[i for i in range(n)]
union=[[]for _ in range(n)]
From_where=[[]for _ in range(n)]
degree=[0]*(n)
adj=[[]for _ in range(n)]
next=[]
#병합부터 실행 >는 다음으로 넘김
for _ in range(m):
    a,b,c=input().split()
    a,c=int(a),int(c)
    if b=='>':
        next.append((a,c))
    else:
        merge(a,c)
#경로 압축
for i in range(n):
    parent[i]=find(i)
#부모노드에 union을 만듬
P=[]
Q=deque([])
for i in range(n):
    union[parent[i]].append(i)
    #부모노드 배열만들기
    if parent[i]==i:
        P.append(i)
#중복이 들어올 수 있으므로 set자료형으로 바꿔줌
for i in P:
    adj[i]=set()
    From_where[i]=set()
#a,c의 값의 부모를 찾아
for a,c in next:
    q=find(a)
    w=find(c)
    adj[w].add(q)
    From_where[q].add(w)
for i in P:
    adj[i]=list(adj[i])
    From_where[i]=list(From_where[i])
    degree[i]=len(From_where[i])
for i in P:
    if degree[i]==0:
        Q.append(i)
cnt=0
while 1:
    if cnt==n:
        print('consistent')
        break
    if not Q:
        print('inconsistent')
        break
    temp=Q.popleft()
    for j in adj[temp]:
        degree[j]-=1
        if degree[j]==0:
            Q.append(j)
    cnt+=len(union[temp])