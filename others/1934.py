from math import lcm
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(lcm(x,y))