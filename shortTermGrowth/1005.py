import sys
from collections import deque
 
T=int(sys.stdin.readline())
 
for _ in range(T):
    N,K=map(int,sys.stdin.readline().split())#건물수, 건설순서규칙
    time=[0]+list(map(int,sys.stdin.readline().split()))#건물들의 건설시간
    seq=[[] for _ in range(N+1)]#건설순서규칙
    inDegree=[0 for _ in range(N+1)]#진입차수
    DP=[0 for _ in range(N+1)]#해당 건물까지 걸리는 시간
 
    for _ in range(K):#건설순서규칙 저장
        a,b=map(int,sys.stdin.readline().split())
        seq[a].append(b)
        inDegree[b]+=1
 
    q = deque()
    for i in range(1,N+1):#진입차수 0인거 찾아서 큐에 넣기
        if inDegree[i]==0:
            q.append(i)
            DP[i]=time[i]
 
    while q:
        a=q.popleft()
        for i in seq[a]:
            inDegree[i]-=1#진입차수 줄이고
            DP[i]=max(DP[a]+time[i],DP[i])#DP를 이용해 건설비용 갱신
            if inDegree[i]==0:
                q.append(i)
 
 
    ans=int(sys.stdin.readline())
    print(DP[ans])