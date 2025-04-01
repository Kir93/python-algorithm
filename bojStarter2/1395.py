import sys
input = sys.stdin.readline

N, M = map(int, input().split())

class LazySegTree() :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self.lazy = [0]*(4*N)

  def propagate(self, start, end, idx) :
    if not self.lazy[idx] :
      return
    if start < end :
      self.lazy[idx*2] = 1 - self.lazy[idx*2]
      self.lazy[idx*2+1] = 1 - self.lazy[idx*2+1]
    self.tree[idx] = end - start + 1 - self.tree[idx]
    self.lazy[idx] = 0
  
  def update(self, left, right) :
    def _update(start, end, idx) :
      self.propagate(start, end, idx)
      if right < start or end < left :
        return
      if left <= start <= end <= right :
        self.lazy[idx] = 1 - self.lazy[idx]
        self.propagate(start, end, idx)
        return

      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _update(0, N-1, 1)

  def search(self, left, right) :
    def _search(start, end, idx) :
      self.propagate(start, end, idx)
      if right < start or end < left : 
        return 0
      if left <= start <= end <= right :
        return self.tree[idx]
      mid = (start + end) // 2
      return _search(start, mid, idx*2) + _search(mid+1, end, idx*2+1)
    print(_search(0, N-1, 1))

segtree = LazySegTree()
for _ in range(M) :
  q, a, b = map(int, input().split())
  if q == 0 :
    segtree.update(a-1, b-1)
  else :
    segtree.search(a-1, b-1)