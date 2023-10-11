s = input()
ls = []
for i in range(0, len(s)-2, 3): ls.append(s[i:i+3])
if len(set(ls)) != len(ls): print('GRESKA')
else:
    r = {'P':13, 'K':13, 'H':13, 'T':13}
    for x in ls:
        card = x[0]
        r[card] -= 1
    print(*r.values())