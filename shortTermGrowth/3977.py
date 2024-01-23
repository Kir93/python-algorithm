import sys, os, io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class UF:
  def __init__(self, n):
    self.p = list(range(n))

  def find(self, a):
    a_ = a
    while a != self.p[a]:
      a = self.p[a]
    while a_ != a:
      self.p[a_], a_ = a, self.p[a_]
    return a

  def merge(self, a, b):
    self.p[self.find(b)] = self.find(a)

def tarjan(G): #O(N+M)
  SCC, S, P = [], [], []
  D = [0] * len(G)
 
  s = [*range(len(G))]
  while s:
    x = s.pop()
    if x < 0:
      d = D[~x] - 1
      if P[-1] > d:
        SCC.append(S[d:])
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
    G[u].append(v)
  
  SCC = {}
  for i, scc in enumerate(tarjan(G)): #O(1)만에 몇 번 SCC에 속하는지 찾을 수 있게 해싱한다. (O(N)
    for v in scc:
      SCC[v] = i 
  
  cnt = i + 1
  uf = UF(cnt)
  IN = [0] * (cnt) #i는 아낌없이 사용한다
  for i, V in enumerate(G): #O(N+M)
    for v in V:
      if SCC[i] != SCC[v]: #외부의 SCC를 가리키고 있는 것이라면
        uf.merge(SCC[i], SCC[v]) #
        IN[SCC[v]] += 1 #해당 SCC의 진입차수를 1 증가시킨다.
    
  if len(set(uf.find(i) for i in range(cnt))) == 1 and IN.count(0) == 1 :
    answer = []
    for k, v in SCC.items() :
      if v == 0 :
        answer.append(k)
    
    sys.stdout.write('\n'.join(map(str, sorted(answer))))
    sys.stdout.write('\n')
  else:
    sys.stdout.write('Confused\n')

T = int(input())
for t in range(T) :
  sol()
  if t != T - 1 :
    input()
    sys.stdout.write('\n')