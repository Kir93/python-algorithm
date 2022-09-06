from sys import stdin, stdout
n = int(stdin.readline())
i = 2
while n != 1:
    if n%i == 0:
        stdout.write(str(i)+'\n')
        n = n//i
    else: i += 1