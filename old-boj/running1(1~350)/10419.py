from math import sqrt
for _ in range(int(input())):
    d = int(input())
    r = 0
    for i in range(int(sqrt(d))+1):
        if i ** 2 + i <= d: r = i
    print(r)