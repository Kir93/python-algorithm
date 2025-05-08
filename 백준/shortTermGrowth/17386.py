import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())


def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0


ans = 0
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) < 0:
    ans = 1
print(ans)