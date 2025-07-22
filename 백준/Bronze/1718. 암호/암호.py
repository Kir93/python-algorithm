s = input()
k = input()
r = []
check = 0

for w in s:
    if w == ' ':
        r.append(w)
    else:
        ord_w = ord(w)
        ord_k = ord(k[check]) - 96
        if ord_w - ord_k < 97:
            r.append(chr((ord_w - ord_k + 26)))
        else:
            r.append(chr(ord_w - ord_k))

    if check == len(k) - 1:
            check = 0
    else:
        check += 1

print(''.join(r))