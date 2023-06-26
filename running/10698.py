for i in range(int(input())):
    x, o, y, _, z = map(str, input().split())
    r = 'YES'
    if o == '+' and int(x) + int(y) != int(z): r = 'NO'
    elif o == '-' and int(x) - int(y) != int(z): r = 'NO'
    print(f'Case {i+1}: {r}')