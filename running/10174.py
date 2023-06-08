for _ in range(int(input())):
    n = input().lower()
    rn = n[::-1]
    if n == rn: print('Yes')
    else: print('No')