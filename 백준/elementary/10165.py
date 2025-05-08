from collections import defaultdict
import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

def init():
  route_list_a = list()
  route_list_b = list()
  for i in range(M) :
    start, end = map(int, input().split())
    if start > end :
      route_list_b.append((i+1, start, end+N))
    else :
      route_list_a.append((i+1, start, end))

  return route_list_a, route_list_b

def traversal(lst, mode = 1) :
  
  lst.sort(key = lambda x : (x[1], -x[2]))
  result = list()
  for idx, start, end in lst :
    if result and result[-1][2] >= end :
      continue
    result.append((idx, start, end))
  
  return result

def extract(lst1, lst2) :
  result = list()
  
  if lst2 :
    result.extend([x[0] for x in lst2])
    _, min_start, _ = lst2[0]
    _, _, max_end = lst2[-1]
    lst1 = [ x for x in lst1 if not ( x[1] >= min_start or x[2] <= max_end-N ) ]

  result.extend([x[0] for x in lst1])
  result.sort()

  return result

route_list_a, route_list_b = init()
result1 = traversal(route_list_a, 1)
result2 = traversal(route_list_b, 2)

result = extract(result1, result2)
print(*result)