import sys
from bisect import *
input = sys.stdin.readline

def cross(f, g):
    return round((g[1] - f[1])/(f[0] - g[0]), 5)

maxX, minX = map(int, input().split())
n = int(input())

stack = []
tmpf = []
for i in range(n):
    upperY, lowY = map(int, input().split())
    dydx = (upperY - lowY) / (maxX - minX)
    jeol = (lowY * maxX - upperY * minX) / (maxX - minX)
    f = [dydx, jeol, minX, i+1]
    tmpf.append(f)

tmpf.sort(key=lambda x:(-x[0], x[1]))

for i in range(n):
    f = tmpf[i]
    if i >= 1 and f[0] == tmpf[i - 1][0]:
        continue

    if stack:
        tmp = cross(f, stack[-1])
        f[2] = tmp

    stack.append(f)
    
    while len(stack) >= 3 and cross(stack[-3], stack[-2]) > cross(stack[-2], stack[-1]):
        stack.pop(-2)

    if len(stack) >= 2:
        stack[-1][2] = cross(stack[-1], stack[-2])

for i in range(int(input())):
    q = float(input())
    idx = bisect_right(stack, q, key = lambda x: x[2]) - 1
    print(stack[idx][3])