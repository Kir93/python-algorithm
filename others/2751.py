from sys import stdin, stdout
ls = []
for _ in range(int(stdin.readline())): ls.append(int(stdin.readline()))
for x in sorted(ls): stdout.write(str(x)+'\n')