c = input()
ls = []
for _ in range(int(input())):
    k = input()
    for i in range(len(c)):
        if c[i] != '*':
            if c[i] != k[i]: break
    else: ls.append(k)
print(len(ls))
print('\n'.join(ls))