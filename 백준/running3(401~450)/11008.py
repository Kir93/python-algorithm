for _ in range(int(input())):
    r = 0
    s, p = map(str, input().split())
    r = s.count(p)
    rs = s.replace(p, '')
    print(r + len(rs))