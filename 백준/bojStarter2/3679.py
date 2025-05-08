import sys;
input = sys.stdin.readline

def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def solve():
    n, *lst = map(int, input().split())

    points = []
    for i in range(n):
        points.append([lst[i * 2], lst[i * 2 + 1], i])

    points.sort()
    used = [False] * n
    convex_hull_down = []
    for i in range(n):
        while len(convex_hull_down) > 1:
            if ccw(convex_hull_down[-2], convex_hull_down[-1], points[i]) >= 0:
                break
            p = convex_hull_down.pop()
            used[p[2]] = False
        convex_hull_down.append(points[i])
        used[points[i][2]] = True

    answer = []
    for x, y, i in points:
        if not used[i]:
            answer.append(i)

    for i in range(len(convex_hull_down) - 1, -1, -1):
        answer.append(convex_hull_down[i][2])

    print(*answer)

for _ in range(int(input())):
    solve()