import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def line_segment_intersection(a, b, c, d):
    def ccw(a, b, c):
        cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if cross_product > 0:
            return 1
        elif cross_product < 0:
            return -1
        else:
            return 0

    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:
        a, b = sorted([a, b])
        c, d = sorted([c, d])
        return not (b < c or d < a)

    return ab <= 0 and cd <= 0


def point_in_non_convex_polygon(p, polygon):
    sp0 = [p[0] + 0.000000000001, p[1] + 0.000000000001]
    sp1 = [p[0] + 1, p[1] + 10 ** 12]
    tmp = 0
    for i in range(len(polygon) - 1):
        if p == polygon[i]:
            return True
        if line_segment_intersection(sp0, sp1, polygon[i], polygon[i + 1]):
            tmp += 1
    if p == polygon[-1]:
        return True
    if line_segment_intersection(sp0, sp1, polygon[-1], polygon[0]):
        tmp += 1
    return tmp & 1 == 1


N = int(input_())
polygon = [list(minput()) for _ in range(N)]

for _ in range(3):
    p = list(minput())
    print(+point_in_non_convex_polygon(p, polygon))