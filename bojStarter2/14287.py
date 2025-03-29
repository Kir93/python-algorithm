from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
children = defaultdict(list)
for i, p in enumerate(map(int, input().split())) :
  children[p-1].append(i)

index = [[0]*2 for _ in range(N)]
tree = [0]*(4*N)
idx = 0
def dfs(node) :
  global idx
  index[node][0] = idx
  for child in children[node] :
    idx += 1
    dfs(child)
  index[node][1] = idx

def update(target, value) :
  start, end, idx = 0, N-1, 1
  while start < end :
    tree[idx] += value
    mid = (start + end) // 2
    if target <= mid :
      end = mid
      idx = idx*2
    else :
      start = mid+1
      idx = idx*2+1
  tree[idx] += value

def search(left, right, start=0, end=N-1, idx=1) :
  if end < left or start > right :
    return 0
  if left <= start <= end <= right :
    return tree[idx]
  mid = (start + end) // 2
  lval = search(left, right, start, mid, idx*2)
  rval = search(left, right, mid+1, end, idx*2+1)
  return lval + rval

dfs(0)
for _ in range(M) :
  q, *cmd = map(int, input().split())
  if q == 1 :
    i, val = cmd
    update(index[i-1][0], val)
  else :
    i = cmd[0]
    print(search(index[i-1][0], index[i-1][1]))