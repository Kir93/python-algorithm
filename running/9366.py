for i in range(1, int(input())+1):
    ls = sorted(map(int, input().split()))
    if ls[0] + ls[1] <= ls[2]: print(f'Case #{i}: invalid!')
    elif ls[0] == ls[1] == ls[2]: print(f'Case #{i}: equilateral')
    elif ls[0] == ls[1] or ls[0] == ls[2] or ls[1] == ls[2]: print(f'Case #{i}: isosceles')
    else: print(f'Case #{i}: scalene')