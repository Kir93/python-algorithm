import sys
input = sys.stdin.readline

M, N = map(int, input().split())
worm_list = [[1]*M for _ in range(M)]
  
def grow_one_day():
  grow_val = list(map(int, input().split()))
  grow_sequence = [0]*grow_val[0] + [1]*grow_val[1] + [2]*grow_val[2]

  return grow_sequence

def grow_all(grow_sequence):
  grow_list = [[0]*M for _ in range(M)]

  for i in range(M): grow_list[-i-1][0] = grow_sequence[i]
  for i in range(M, 2*M-1): grow_list[0][i+1-M] = grow_sequence[i]

  for i in range(1, M):
    for j in range(1, M): grow_list[i][j] = grow_list[i-1][j]

  return grow_list

def grow_full_day():
  full_grow_sequence = [0]*(2*M-1)
  for _ in range(N):
    grow_sequence = grow_one_day()
    for i in range(2*M-1): full_grow_sequence[i] += grow_sequence[i]

  grow_list = grow_all(full_grow_sequence)
  
  for i in range(M):
    for j in range(M): worm_list[i][j] += grow_list[i][j]

grow_full_day()
for worm in worm_list: print(*worm)