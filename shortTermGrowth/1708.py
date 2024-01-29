def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return c > 0

def convex_hull(positions):
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(*p1, *p2, *p3):
                break
            convex.pop()
        convex.append(p3)

    return len(convex)

n = int(input())
positions = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
print(convex_hull(positions) + convex_hull(positions[::-1]) - 2)
