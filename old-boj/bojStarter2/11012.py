from array import array
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    xs = [0] * n
    ys = [0] * n
    for i in range(n):
        xs[i], ys[i] = map(int, input().split())
    
    comp_x = sorted(set(xs))
    comp_y = sorted(set(ys))
    X = len(comp_x)
    Y = len(comp_y)

    prefix = array('h', [0]) * ((X + 1) * (Y + 1))
    for i in range(n):
        ix = bisect_left(comp_x, xs[i]) + 1
        iy = bisect_left(comp_y, ys[i]) + 1
        prefix[ix * (Y+1) + iy] += 1


    for i in range(1, X + 1):
        base = i * (Y+1)
        prev = (i-1) * (Y+1)
        for j in range(1, Y + 1):
            prefix[base + j] += prefix[prev + j] + prefix[base + j - 1] - prefix[prev + j - 1]
    
    res = 0
    for _ in range(m):
        x1, x2, y1, y2 = map(int, input().split())
        x1 = bisect_left(comp_x, x1) + 1
        x2 = bisect_right(comp_x, x2)
        y1 = bisect_left(comp_y, y1) + 1
        y2 = bisect_right(comp_y, y2)
        if x1 > x2 or y1 > y2:
            continue
        
        res += prefix[x2*(Y+1)+y2]-prefix[(x1-1)*(Y+1)+y2]-prefix[x2*(Y+1)+(y1-1)]+prefix[(x1-1)*(Y+1)+(y1-1)]
    
    print(res)
    

T = int(input())
for _ in range(T):
    solve()