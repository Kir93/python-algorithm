c = list(input())
ls = []
for _ in range(int(input())):
    k = list(input())
    f = True
    for i in range(len(c)):
        if c[i] == '*': continue
        elif c[i] != k[i]:
            f = False
            break
    if f == True: ls.append(k)
print(len(ls))
for x in ls: print(''.join(x))