k = int(input())
s = input()
ls = []
for i in range(0, len(s), k):
    ls.append(list(s[i:i+k]))
for i in range(len(ls)):
    if i % 2 != 0:
        data = list(reversed(ls[i]))
        ls[i] = data
r = ''
for i in range(k):
    for j in range(len(ls)):
        r += ls[j][i]
print(r)