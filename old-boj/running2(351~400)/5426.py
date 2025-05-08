for _ in range(int(input())):
    s = input()
    ls = []
    for i in range(0, len(s), int(len(s)**0.5)):
        ls.append(s[i:i+int(len(s)**0.5)])
    for i in range(int(len(s)**0.5)-1, -1, -1):
        for j in range(int(len(s)**0.5)):
            print(ls[j][i], end='')
    print('')