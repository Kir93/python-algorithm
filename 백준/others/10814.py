from sys import stdin, stdout
ls = []
for _ in range(int(stdin.readline())):
    ls.append(list(map(str, stdin.readline().split())))
for x, y in sorted(ls, key=lambda x:int(x[0])): stdout.write(x+' '+y+'\n')