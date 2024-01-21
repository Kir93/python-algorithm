import sys

sdr = sys.stdin.readline
sdw = sys.stdout.write

V,E = map(int,sdr().split())
prev = [0]*(V+1)
vdf = [[i,0,0] for i in range(V+1)]
edges = [[1] for _ in range(V+1)]
reverseEdges = [[] for _ in range(V+1)]
for _ in range(E):
    u,v = map(int,sdr().split())
    edges[u].append(v)
    reverseEdges[v].append(u)
t = 0    
for i in range(1,V+1):
    if vdf[i][2] > 0: continue
    u = i
    t += 1
    vdf[u][1] = t
    while vdf[i][2] == 0:
        if edges[u][0] < len(edges[u]):
            v = edges[u][edges[u][0]]
            edges[u][0] += 1    
            if vdf[v][1] == 0:
                t += 1
                vdf[v][1] = t
                prev[v] = u
                u = v
        else:
            t += 1
            vdf[u][2] = t
            u = prev[u]
vdf = sorted(vdf,key=lambda x:x[2],reverse=True)
sccs = []
for i in range(V):
    u = vdf[i][0]
    if prev[u] == -1: continue
    path = [u]
    prev[u] = -1
    j = 0
    while j < len(path):
        u = path[j]
        for v in reverseEdges[u]:
            if prev[v] != -1:
                path.append(v)
                prev[v] = -1
        j += 1
    path.sort()
    sccs.append(path)
sdw(f"{len(sccs)}\n")
sccs.sort()
for scc in sccs:
    for e in scc:
        sdw(f"{e} ")
    sdw(f"{-1}\n")