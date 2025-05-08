n = int(input())
ls = list(map(int, input().split()))
for i in ls:
    if i<2:
        n-=1
        pass
    for j in range(2, i):
        if i%j ==0:
            n-=1
            break
print(n)