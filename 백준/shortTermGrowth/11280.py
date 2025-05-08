import sys, io, os
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
 
class TwoSat:
  def __init__(self, n):
    self.n = n
    self.graph = [[] for _ in range(2 * n)]
 
  def _imply(self, x, y):
    self.graph[x].append(y if y >= 0 else 2 * self.n + y)
 
  def either(self, x, y):
    """either x or y must be True"""
    self._imply(~x, y)
    self._imply(~y, x)
 
  def set(self, x):
    """x must be True"""
    self._imply(~x, x)
 
  def solve(self):
    SCC = tarjan(self.graph)
    order = [0] * (2 * self.n)
    for i, comp in enumerate(SCC):
      for x in comp:
        order[x] = i
    for i in range(self.n):
      if order[i] == order[~i]:
        return False, None
    return True, [+(order[i] > order[~i]) for i in range(self.n)]

N, M = map(int, input().split())
ts = TwoSat(N)
for _ in range(M):
  a, b = map(lambda x: int(x)-1 if int(x) > 0 else int(x), input().split())
  ts.either(a, b)
ok, ans = ts.solve()
sys.stdout.write("1\n" if ok else "0\n")