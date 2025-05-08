l = list(map(int, input().split()))
l.sort()
x = list(input())
ls = []
for s in x:
    if s == 'A': ls.append(l[0])
    elif s == 'B': ls.append(l[1])
    elif s == 'C': ls.append(l[2])
print(*ls)