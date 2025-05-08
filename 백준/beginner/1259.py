while True:
    x = input()
    if x == '0': break
    elif x == x[::-1]: print('yes')
    else: print('no')