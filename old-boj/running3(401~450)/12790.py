for _ in range(int(input())):
    li = list(map(int, input().split()))
    s = [li[i] + li[i+4] for i in range(4)]
    res = max(s[0], 1) + max(s[1], 1)*5 + max(s[2], 0)*2 + s[3]*2
    print(res)