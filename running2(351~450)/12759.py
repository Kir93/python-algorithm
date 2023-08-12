from itertools import combinations


def findWinner(p, t):
    sorted_li = sorted(t)
    ls = [(1,2,3), (4,5,6), (7,8,9), (1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    comb = list(combinations(sorted_li, 3))
    for com in comb:
        if com in ls: return p
    return 0

num = {(1,1):1, (1,2):2, (1,3):3, (2,1):4, (2,2):5, (2,3):6, (3,1):7, (3,2):8, (3,3):9}
first = []
last = []
winner = 0
draw = 0
p1 = int(input())
p2 = 2 if p1 == 1 else 1

for i in range(1, 10):
    a, b = map(int, input().split())
    if i%2 != 0:
        first.append(num[(a,b)])
        if i >= 5:
            winner = findWinner(p1, first)
            if winner != 0:
                print(winner)
                draw = winner
                break
    else:
        last.append(num[(a,b)])
        if i >= 6:
            winner = findWinner(p2, last)
            if winner != 0:
                print(winner)
                draw = winner
                break

if draw == 0: print(0)