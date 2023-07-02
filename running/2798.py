# from itertools import combinations
# n, m = map(int, input().split())
# ls = list(map(int, input().split()))
# r = [sum(t) for t in combinations(ls, 3) if sum(t) <= m]
# print(max(r))

n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())), reverse=True)
r = 0
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        for z in range(j+1, len(ls)):
            t = sum([ls[i], ls[j], ls[z]])
            if t < m: r = max(r, t)
            elif t == m:
                r = t
                exit(print(r))
print(r)