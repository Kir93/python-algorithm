T = int(input())
for _ in range(T):
    N = int(input())
    res = 0
    for i in range(N):
        if i % 2 == 1:
            res += i
    print(res+N)