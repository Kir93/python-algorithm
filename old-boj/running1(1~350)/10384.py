alphabet = list(range(97, 123))
for i in range(1, int(input())+1):
    w = input().lower()
    check = [0] * 26
    for x in w:
        key = ord(x)
        if key in alphabet: check[key - 97] += 1
    if min(check) == 0: print(f'Case {i}: Not a pangram')
    elif min(check) == 1: print(f'Case {i}: Pangram!')
    elif min(check) == 2: print(f'Case {i}: Double pangram!!')
    elif min(check) == 3: print(f'Case {i}: Triple pangram!!!')