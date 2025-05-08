from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
ls = []
for _ in range(int(input())):
    n = int(input())
    if n == 0 and len(ls): print(heappop(ls)[1])
    elif n == 0 and len(ls) == 0: print(0)
    else:
         heappush(ls, (abs(n), n))