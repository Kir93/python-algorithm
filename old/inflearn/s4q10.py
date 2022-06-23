import sys
import heapq as hq
#sys.stdin = open("input.txt", "r")
hip = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(hip) == 0:
            print(-1)
        else:
            print(hq.heappop(hip))
    else:
        hq.heappush(hip, n)
