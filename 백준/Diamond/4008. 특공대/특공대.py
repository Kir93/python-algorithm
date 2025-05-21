import sys
from collections import deque

def T(i, j, A, B):
    c, d = i
    e, f = j
    return (A * (e ** 2 - c ** 2) - B * (e - c) + f - d) / (2 * A * (e - c))

input = sys.stdin.read
data = input().split()

N = int(data[0])
A, B, C = map(int, data[1:4])
values = list(map(int, data[4:]))

pre_sum = 0
dp = 0
E = deque([(0, 0)])

for t in values:
    pre_sum += t 
    

    while len(E) > 1 and T(E[0], E[1], A, B) < pre_sum:
        E.popleft()
    

    e, f = E[0]
    dp = -2 * A * e * pre_sum + A * e ** 2 - B * e + f + A * pre_sum ** 2 + B * pre_sum + C
    

    while len(E) > 1 and T((pre_sum, dp), E[-2], A, B) < T(E[-1], E[-2], A, B):
        E.pop()
    

    E.append((pre_sum, dp))

print(E[-1][1])