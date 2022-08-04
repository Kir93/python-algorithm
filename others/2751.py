from sys import stdin, stdout
ls = []
for _ in range(int(input())):
    ls.append(int(stdin.readline()))
for i in sorted(ls):
    stdout.write(str(i)+'\n')