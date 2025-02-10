import sys
input = sys.stdin.readline

point = []
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

point.append([x1, y1])
point.append([x2, y2])
point.append([x3, y3])
point.append([x4, y4])

def check(a, b, c, d):
    if ccw(a, b, c) * ccw(a, b, d) == 0:
        if ccw(c, d, a) * ccw(c, d, b) == 0:
            if a > b:
                a, b = b, a
            if c > d:
                c, d = d, c
            if b >= c and a <= d:
                return True
            else:
                return False
    if ccw(a, b, c) * ccw(a, b, d) <= 0:
        if ccw(c, d, a) * ccw(c, d, b) <= 0:
            return True
    return False

def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])

if check(point[0], point[1], point[2], point[3]):
    print(1)
    try:
        x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        print(x, y)
    except:
        if point[0] > point[1]:
            point[0], point[1] = point[1], point[0]
        if point[2] > point[3]:
            point[2], point[3] = point[3], point[2]
        if point[1] == point[2]:
            print(point[1][0], point[1][1])
        elif point[0] == point[3]:
            print(point[0][0], point[0][1])
else:
    print(0)