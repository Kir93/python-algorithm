from sys import stdin
ls = []
for _ in range(int(stdin.readline())):
    c = stdin.readline().split()
    if c[0]=='push': ls.append(c[1])
    elif c[0]=='pop':
        if len(ls): print(ls.pop())
        else: print(-1)
    elif c[0]=='size': print(len(ls))
    elif c[0]=='empty':
        if len(ls): print(0)
        else: print(1)
    elif c[0]=='top':
        if len(ls): print(ls[-1]) 
        else: print(-1)