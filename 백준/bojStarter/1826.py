from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
oil_list = [list(map(int, input().split())) for _ in range(N)]
oil_list.sort( key = lambda x : (x[0], -x[1]))
L, P = map(int, input().split())
oil_list.append([L, 0])
oil_heap = list()
cnt = 0

for l, p in oil_list :
  if P >= L :
    break
  while P < l and oil_heap :
    P += -heappop(oil_heap)
    cnt += 1
  if P < l :
    break
  heappush(oil_heap, -p)

print(cnt if P >= L else -1)