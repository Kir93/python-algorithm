for _ in range(int(input())):
    a, b = map(str, input().split())
    x = sorted(list(a))
    y = sorted(list(b))
    if x == y: print(f'{a} & {b} are anagrams.')
    else: print(f'{a} & {b} are NOT anagrams.')