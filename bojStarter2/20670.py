import sys;
input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    
def is_inside_convex(hull, point):

    st = 2; en = len(hull) - 1
    while st < en:
        mid = (st + en) >> 1
        if ccw(hull[0], hull[mid], point) < 0:
            en = mid
        else:
            st = mid + 1

    return ccw(hull[0], hull[st - 1], point) >= 0 and ccw(hull[st - 1], hull[st], point) >= 0 and ccw(hull[st], hull[0], point) >= 0

N, M, K = map(int, input().split())
P = list(map(int, input().split()))
A = [(P[i << 1], P[i << 1 | 1]) for i in range(N)]
P = list(map(int, input().split()))
B = [(P[i << 1], P[i << 1 | 1]) for i in range(M)]
P = list(map(int, input().split()))
points = [(P[i << 1], P[i << 1 | 1]) for i in range(K)]

result = 0
for point in points:
    if not is_inside_convex(A, point) or is_inside_convex(B, point):
        result += 1

print(result if result else "YES")