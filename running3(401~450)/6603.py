from itertools import combinations
while True:
    ls = list(map(int, input().split()))
    k = ls[0]
    s = ls[1:]
    for i in combinations(s, 6):
        print(*i)
    if k == 0: break
    print()