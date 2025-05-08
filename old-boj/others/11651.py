from sys import stdin, stdout
ls = []
for _ in range(int(stdin.readline())):
    ls.append(list(map(int, stdin.readline().split())))
for x,y in sorted(ls, key=lambda x:(x[1], x[0])): stdout.write(str(x)+' '+str(y)+'\n')
