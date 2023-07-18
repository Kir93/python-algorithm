for _ in range(int(input())):
    perm = list(input())
    flag = False
    for i in range(len(perm)-1, 0, -1):
        if flag: break
        if ord(perm[i-1]) < ord(perm[i]):
            for j in range(len(perm)-1, 0, -1):
                if ord(perm[i-1]) < ord(perm[j]):
                    perm[i-1], perm[j] = perm[j], perm[i-1]
                    perm = perm[:i] + sorted(perm[i:])
                    flag = True
                    break
    print(''.join(perm))