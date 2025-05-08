import sys
import math
input = sys.stdin.readline

x, y, d, t = map(int, input().split())
dist = math.sqrt(x**2+y**2)

if dist >= d: answer = min(t*(dist//d)+dist%d, t*(dist//d+1),dist)
else: answer = min(t+(d-dist), 2*t,dist)

print(answer)