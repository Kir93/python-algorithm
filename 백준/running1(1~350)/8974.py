a, b = map(int, input().split())
ls = []
for i in range(1, b+1):
    if len(ls) < b:
        for _ in range(i):
            ls.append(i)
print(sum(ls[a-1:b]))