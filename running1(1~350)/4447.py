for _ in range(int(input())):
    w = input()
    x = w.lower()
    if x.count('g') > x.count('b'): print(f'{w} is GOOD')
    elif x.count('g') < x.count('b'): print(f'{w} is A BADDY')
    else: print(f'{w} is NEUTRAL')