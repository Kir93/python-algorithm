import sys

input = sys.stdin.readline

def ccw(a, b, c): 
    if (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0]) > 0:
        return True
    return False

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
    C = int(input())
    if C == 2:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(dist(a, b) ** 0.5)
        return
    
    arrows = sorted(list(map(int, input().split())) for _ in range(C))
    convex_hull_down = []
    for i in range(C):
        while len(convex_hull_down) > 1:
            if ccw(convex_hull_down[-2], convex_hull_down[-1], arrows[i]):
                break
            convex_hull_down.pop()
        convex_hull_down.append(arrows[i])
    convex_hull_up = []
    for i in range(C - 1, -1, -1):
        while len(convex_hull_up) > 1:
            if ccw(convex_hull_up[-2], convex_hull_up[-1], arrows[i]):
                break
            convex_hull_up.pop()
        convex_hull_up.append(arrows[i])
    lp, rp = 0, len(convex_hull_down) - 1
    convex_hull = convex_hull_down[:-1] + convex_hull_up[:-1] 

    answer = dist(convex_hull[lp], convex_hull[rp])
    size = len(convex_hull) # 볼록 껍질의 크기
    for _ in range(size):
        lx, ly = convex_hull[lp]
        llx, lly = convex_hull[(lp + 1) % size]
        rx, ry = convex_hull[rp]
        rrx, rry = convex_hull[(rp + 1) % size]
        if ccw([llx - lx, lly - ly], [0, 0], [rrx - rx, rry - ry]):
            lp = (lp + 1) % size
        else:
            rp = (rp + 1) % size
        answer = max(answer, dist(convex_hull[lp], convex_hull[rp]))
    print(answer ** 0.5) 

solve()