import sys
input = sys.stdin.readline

N, M = map(int, input().split())
children = [list() for _ in range(N+1)]
parents = [[0, 0] for _ in range(N+1)]
index = [[0, 0] for _ in range(N+1)]
salary = [0]*(N+1)

def dfs():
  q = [(1, 0)]
  leaf_q = []
  cnt = 0
  while q:
    n, p = q.pop()
    cnt += 1
    index[n][0] = cnt
    if not children[n]:
      leaf_q.append(n)
      index[n][1] = cnt
      continue
    for c in children[n]:
      q.append((c, n))
  while leaf_q:
    n = leaf_q.pop()
    p = parents[n][0]
    if p :
      if index[p][1] < index[n][1] :
        index[p][1] = index[n][1]
      parents[p][1] -= 1
      if not parents[p][1] :
        leaf_q.append(p)

def propagate(start, end, idx):
  if start != end:
    lazy[idx*2 + 1] += lazy[idx]
    lazy[idx*2] += lazy[idx]
  else:
    tree[idx] += lazy[idx]
  lazy[idx] = 0

def update(left, right, val):
  q = [(0, N, 1)]
  while q :
    s, e, i = q.pop()
    propagate(s, e, i)
    if left > e or right < s :
      continue
    if left <= s <= e <= right :
      lazy[i] += val
      continue
    mid = (s + e) // 2
    q.append((s, mid, i*2))
    q.append((mid+1, e, i*2+1))

def search(target):
  start, end, idx = 0, N, 1
  while start < end:
    propagate(start, end, idx)
    mid = (start + end) // 2
    if target <= mid:
      end = mid
      idx = idx*2
    else :
      start = mid+1
      idx = idx*2+1
  propagate(start, end, idx)
  return tree[idx]

arr = [-1]+list(map(int,input().split()))
for i in range(2, N + 1):
  p = arr[i]
  parents[i][0] = p
  parents[p][1] += 1
  children[p].append(i)

dfs()
tree = [0]*(4*N + 4)
lazy = [0]*(4*N + 4)

for _ in range(M):
  q, *cmd = map(int,input().split())
  if q == 1:
    a, b = cmd
    left, right = index[a]
    update(left, right, b)
  else:
    a = cmd[0]
    result = search(index[a][0])
    print(result)