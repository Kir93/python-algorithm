import sys
from collections import deque
input=sys.stdin.readline

def MCMF(source,sink,loop):
    global money
    for _ in range(loop):
        v=len(G)
        visit=[-1]*v
        d=[10**9]*v
        d[source]=0
        queue=deque([source])
        in_queue=[False]*v
        while queue:
            u=queue.popleft()
            in_queue[u]=False
            for end,cost in G[u]:
                if d[u]+cost<d[end] and C[u][end]-F[u][end]>0:
                    d[end]=d[u]+cost
                    visit[end]=u
                    if in_queue[end]==False:
                        queue.append(end)
                        in_queue[end]=True
        a=sink
        while a!=source:
            b=visit[a]
            F[b][a]+=1
            F[a][b]-=1
            a=b
        #for i in F:
            #print(i)
        money+=d[sink]
for _ in range(int(input())):
    V,E=map(int,input().split())
    G=[[] for _ in range(V*2+3)]
    C=[[0]*(V*2+3) for _ in range(V*2+3)]
    F=[[0]*(V*2+3) for _ in range(V*2+3)]
    money=0
    source=V+1
    sink=V+2
    for i in range(E):
        a,b=map(int,input().split())
        C[-a][b]=10**9
        C[-b][a]=10**9
        G[-a].append((b,1))
        G[b].append((-a,-1))
        G[-b].append((a,1))
        G[a].append((-b,-1))
    B_V=list(map(int,input().split()))
    B_C=list(map(int,input().split()))
    for i in range(1,V+1):
        C[i][-i]=10**9
        G[i].append((-i,0))
        G[-i].append((i,0))
        if B_C[i-1]==0 and B_V[i-1]==1:
            G[source].append((i,0))
            #G[-i].append((source,0))
            C[source][i]=1
        if B_C[i-1]==1 and B_V[i-1]==0:
            G[-i].append((sink,0))
            #G[sink].append((-i,0))
            C[-i][sink]=1
    MCMF(source,sink,len(G[source]))
    print(money)