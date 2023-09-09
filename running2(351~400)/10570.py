for _ in range(int(input())):
    l = [0] * 1001
    for _ in range(int(input())):
        l[int(input())] += 1
    print(l.index(max(l)))