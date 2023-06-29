def sumNum(x):
    r = 0
    for c in x:
        if c.isdigit(): r += int(c)
    return r

ls = []

for _ in range(int(input())):
    ls.append(input())
ls.sort(key=lambda x:(len(x), sumNum(x), x))

for w in ls: print(w) 