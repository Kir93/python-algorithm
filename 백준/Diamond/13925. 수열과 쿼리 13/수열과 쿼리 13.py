import sys
input = sys.stdin.readline
MOD = int(1e9) + 7

N = int(input())
nums = list(map(int, input().split()))
tree = [0]*(4*N+4)
lazy = [[1, 0] for _ in range(4*N+4)]
def init(start = 0, end = N-1, idx = 1) :
  if start == end :
    tree[idx] = nums[start]
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)  
  tree[idx] = tree[idx*2] + tree[idx*2+1]

def propagate(start, end, idx) :
  if start != end :
    for i in range(2) :
      lazy[idx*2][i] = (lazy[idx*2][i]*lazy[idx][0]) % MOD
      lazy[idx*2+1][i] = (lazy[idx*2+1][i]*lazy[idx][0]) % MOD
    lazy[idx*2][1] = (lazy[idx*2][1] + lazy[idx][1]) % MOD
    lazy[idx*2+1][1] = (lazy[idx*2+1][1] + lazy[idx][1]) % MOD
  tree[idx] = (tree[idx] * lazy[idx][0]) % MOD
  tree[idx] = (tree[idx] + lazy[idx][1]*(end - start + 1)) % MOD
  lazy[idx][0] = 1
  lazy[idx][1] = 0

def update(left, right, val, ops, start = 0, end = N-1, idx = 1) :
  propagate(start, end, idx)
  if right < start or left > end :
    return
  if left <= start <= end <= right :
    if ops == 1 :
      lazy[idx][1] = (lazy[idx][1] + val) % MOD
    elif ops == 2 :
      lazy[idx][0] = (lazy[idx][0] * val) % MOD
      lazy[idx][1] = (lazy[idx][1] * val) % MOD
    else :
      lazy[idx][0] = 0
      lazy[idx][1] = val
    propagate(start, end, idx)
    return
  mid = (start + end) // 2
  update(left, right, val, ops, start, mid, idx*2)
  update(left, right, val, ops, mid+1, end, idx*2+1)
  tree[idx] = (tree[idx*2] + tree[idx*2+1]) % MOD

def search(left, right, start = 0, end = N-1, idx = 1) :
  propagate(start, end, idx)
  if right < start or left > end :
    return 0
  if left <= start <= end <= right :
    return tree[idx] % MOD
  mid = (start + end) // 2
  ret = 0
  ret = (ret + search(left, right, start, mid, idx*2)) % MOD
  ret = (ret + search(left, right, mid+1, end, idx*2+1)) % MOD
  return ret

init()

for _ in range(int(input())) :
  q, *cmd = map(int, input().split())
  if q <= 3 :
    x, y, v = cmd
    update(x-1, y-1, v, q)
  else :
    x, y = cmd
    print(search(x-1, y-1) % MOD)