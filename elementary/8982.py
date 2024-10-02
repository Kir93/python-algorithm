from collections import defaultdict
import sys
input = sys.stdin.readline

def water_init() :
  prev_y = -1
  N = int(input())
  water_list = list()
  depth_list = list()
  for x, y in [map(int, input().split()) for _ in range(N)] :
    if y == prev_y :
      for _ in range(x - prev_x) :
        water_list.append(prev_y)
        depth_list.append(prev_y)
    prev_x, prev_y = x, y

  return water_list, depth_list

def hole_init() :
  K = int(input())
  hole_list = [list(map(int, input().split())) for _ in range(K)]

  return hole_list
  
def sink_water(depth_list, water_list, sx, ex, y) :
  length = len(water_list)
  for x in range(sx, ex) :
    water_list[x] = 0

  min_sinked = y
  for x in range(sx-1, -1, -1) :
    min_sinked = min(min_sinked, depth_list[x])
    water_list[x] = min(water_list[x], depth_list[x] - min_sinked)

  min_sinked = y
  for x in range(ex, length) :
    min_sinked = min(min_sinked, depth_list[x])
    water_list[x] = min(water_list[x], depth_list[x] - min_sinked)

def full_sink(water_list, depth_list, hole_list) :
  for sx, y, ex, _ in hole_list :
    sink_water(depth_list, water_list, sx, ex, y)


water_list, depth_list = water_init()
hole_list = hole_init()
full_sink(water_list, depth_list, hole_list)
print(sum(water_list))
