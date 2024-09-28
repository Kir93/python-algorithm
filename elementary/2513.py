from collections import deque
import sys
input = sys.stdin.readline

N, K, S = map(int, input().split())
left_q, right_q = list(), list()

def service(q) :
  if not q :
    return 0

  max_dist = 0
  result = 0
  left = K
  
  while q :
    dist, num = q.pop()
    max_dist = max(dist, max_dist)
    if left < num :
      result += max_dist*2
      q.append((dist, num - left))
      max_dist = 0
      left = K
    else :
      left -= num

  return result + max_dist*2

for _ in range(N) :
  coord, num = map(int, input().split())
  if coord < S :
    left_q.append((S - coord, num))
  else :
    right_q.append((coord - S, num))

left_q = deque(sorted(left_q))
right_q = deque(sorted(right_q))

result = service(left_q) + service(right_q)
print(result)