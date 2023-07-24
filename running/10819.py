from itertools import permutations

n = int(input())
r = 0
ls = list(map(int, input().split()))

for i in permutations(ls):
    t = 0
    for j in range(1, n):
        t += abs(i[j-1] - i[j])
        if t > r: r = t

print(r)