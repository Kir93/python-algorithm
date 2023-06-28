for i in range(int(input())):
    h = int(input())
    l = input()
    for c in l:
        h -= 1
        if c == 'c': h += 2
    print(f'Data Set {i+1}:')
    print(h)
    print()