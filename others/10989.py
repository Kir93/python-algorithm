# append 말고 0을 대입한 뒤 추가해 주는 방식으로 풀자.
# stdin, stdout 이용해야 됨.
from sys import stdin, stdout
ls = [0 for _ in range(10001)]
for _ in range(int(stdin.readline())):
    ls[int(stdin.readline())] += 1
for i in range(10001):
    if ls[i] != 0:
        for _ in range(ls[i]):
            stdout.write(str(i)+'\n')