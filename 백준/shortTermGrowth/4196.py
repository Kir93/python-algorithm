import sys, os, io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def tarjan(G):
  SCC, S, P = [], [], []
  D = [0] * len(G)
 
  s = [*range(len(G))]
  while s:
    x = s.pop()
    if x < 0:
      d = D[~x] - 1
      if P[-1] > d:
        SCC.append( sorted(S[d:]) )
        del S[d:], P[-1]
        for x in SCC[-1]:
          D[x] = -1
    elif D[x] > 0:
      while P[-1] > D[x]:
        P.pop()
    elif D[x] == 0:
      S.append(x)
      P.append(len(S))
      D[x] = len(S)
      s.append(~x)
      s += G[x]
  return SCC[::-1]

def sol():
  N, M = map(int, input().split())
  G = [[] for _ in range(N)]
  for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
  
  SCC = {}
  for i, scc in enumerate(tarjan(G)):
    for v in scc:
      SCC[v] = i 
  
  IN = [0] * (i + 1)
  for i, V in enumerate(G):
    for v in V:
      if SCC[i] != SCC[v]:
        IN[SCC[v]] += 1
  
  sys.stdout.write(str(IN.count(0)) + '\n')

for _ in range(int(input())) :
  sol()