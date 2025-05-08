import sys
from collections import Counter

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


def direction(a: Point, b: Point, c: Point):
    dxab = b.x - a.x
    dxac = c.x - a.x
    dyab = b.y - a.y
    dyac = c.y - a.y

    # AB 기울기 > AC 기울기
    if dxab * dyac < dyab * dxac:
        dir = 1
    # AB 기울기 < AC 기울기
    elif dxab * dyac > dyab * dxac:
        dir = -1
    # AB 기울기 == AC 기울기
    else:
        if dxab == 0 and dyab == 0:
            dir == 0
        if dxab * dxac < 0 or dyab * dyac < 0:
            dir = -1
        elif dxab * dxab + dyab * dyab >= dxac * dxac + dyac * dyac:
            dir = 0
        else:
            dir = 1
    return dir


def intersection(l1: Line, l2: Line):
    if direction(l1.p1, l1.p2, l2.p1) * direction(l1.p1, l1.p2, l2.p2) <= 0 and \
            direction(l2.p1, l2.p2, l1.p1) * direction(l2.p1, l2.p2, l1.p2) <= 0:
        return True
    return False


# N개의 선분
N = int(input())

lines = []
parent = [i for i in range(N)]

for i in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    line = Line(Point(x1, y1), Point(x2, y2))
    lines.append(line)

for i in range(N):
    for j in range(i+1, N):
        if intersection(lines[i], lines[j]):
            union_parent(parent, i, j)

parent = [find_parent(parent, x) for x in parent]

cnt = Counter(parent)
print(len(cnt))     # 그룹의 수
print(max(cnt.values()))        # 가장 크기가 큰 그룹에 속하는 선분의 개수