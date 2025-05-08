for _ in range(int(input())):
    ls = [0, 0, 0, 0, 0, 0, 0, 0]
    c = list(input())
    for i in range(2, len(c)):
        if c[i-2] == c[i-1] == c[i] == 'T': ls[0] += 1
        elif c[i-2] == c[i-1] == 'T' and c[i] == 'H': ls[1] += 1
        elif c[i-2] == c[i] == 'T' and c[i-1] == 'H': ls[2] += 1
        elif c[i-1] == c[i] == 'H' and c[i-2] == 'T': ls[3] += 1
        elif c[i-1] == c[i] == 'T' and c[i-2] == 'H': ls[4] += 1
        elif c[i-2] == c[i] == 'H' and c[i-1] == 'T': ls[5] += 1
        elif c[i-2] == c[i-1] == 'H' and c[i] == 'T': ls[6] += 1
        elif c[i-2] == c[i-1] == c[i] == 'H': ls[7] += 1
    print(*ls)