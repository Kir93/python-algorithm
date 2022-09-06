n = int(input())
N = n
if n == 1: exit()
while N > 1:
    for i in range(2, n+1):
        if N%i==0:
            print(i)
            N = N//i
            break