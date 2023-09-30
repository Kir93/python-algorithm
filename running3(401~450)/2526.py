n, p = map(int, input().split())
ls = []
r = n
while True:
    r = (r*n)%p
    if r in ls:
        print(len(ls) - ls.index(r))
        break
    ls.append(r)