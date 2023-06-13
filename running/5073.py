while True:
    ls = sorted(list(map(int, input().split())))
    if sum(ls) == 0: break
    if ls[0] == ls[1] == ls[2]: print('Equilateral')
    elif ls[0] + ls[1] <= ls[2]: print('Invalid')
    elif ls[0] == ls[1] or ls[0] == ls[2] or ls[1] == ls[2]: print('Isosceles')
    else: print('Scalene')