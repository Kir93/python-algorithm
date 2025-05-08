import sys; input = sys.stdin.readline
from math import pi

def ccw(a, b, c): # a-b-c가 반시계 방향인지 검사
    if (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0]) > 0:
        return True
    return False

def dist(a, b): # a-b 거리 계산 (제곱 형태로 반환)
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
    N, L = map(int, input().split())
    # 건물들의 좌표가 x, y 오름차순이 되게 정렬한다.
    buildings = sorted(list(map(int, input().split())) for _ in range(N))

    # monotone chain
    # 볼록 껍질의 아래
    convex_hull_down = []
    for i in range(N):
        while len(convex_hull_down) > 1:
            if ccw(convex_hull_down[-2], convex_hull_down[-1], buildings[i]):
                break
            convex_hull_down.pop()
        convex_hull_down.append(buildings[i])
    # 볼록 껍질의 위
    convex_hull_up = []
    for i in range(N - 1, -1, -1):
        while len(convex_hull_up) > 1:
            if ccw(convex_hull_up[-2], convex_hull_up[-1], buildings[i]):
                break
            convex_hull_up.pop()
        convex_hull_up.append(buildings[i])
    # 볼록 껍질의 아래와 위를 합치자.
    # 양 끝점이 겹치는데, 모든 선분의 길이를 확인해야 하므로 시작점은 끝에 한번 더 넣자.
    convex_hull = convex_hull_down[:-1] + convex_hull_up
    # 볼록 껍질의 각 선분의 길이의 합과 반지름 L인 원의 둘레를 합하여 출력
    print(format(sum(dist(convex_hull[i], convex_hull[i + 1]) ** 0.5 for i in range(len(convex_hull) - 1)) + 2 * pi * L, '.0f'))

solve()