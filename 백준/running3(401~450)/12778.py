for _ in range(int(input())):
    n, c = map(str, input().split())
    ls = list(map(str, input().split(' ')))
    if c == 'C':
        for x in ls: print(ord(x) - 64, end=' ') 
    else:
        for x in ls: print(chr(int(x) + 64), end=' ')
    print()