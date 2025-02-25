L = []
N, M = map(int, input().split())
for _ in range(N):
    s, e  =map(int, input().split())
    if s>e : 
        L.append([e,s])

L.sort(key = lambda x: -x[1])
tmp = []
ts, te = L[0]
for i in range(1,len(L)):
    s,e = L[i]
    
    if ts <= e : # <=te (sort에 의해 보장됨)
        ts = min(ts,s)
    
    else:   #e < ts 
        tmp.append([ts,te])
        ts, te = s,e

tmp.append([ts,te])

answer = M
for i in range(len(tmp)):
    answer += 2*(tmp[i][1] - tmp[i][0])
    
print(answer)