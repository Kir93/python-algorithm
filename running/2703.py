for _ in range(int(input())):
    s = list(input())
    c = list(input())
    for i in range(len(s)):
        if s[i] == ' ': continue
        else:
            s[i] = c[ord(s[i])-65]
    print(''.join(s))