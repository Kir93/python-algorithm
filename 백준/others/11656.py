s = list(input())
ls = []
for i in range(len(s)): ls.append("".join(s[i:len(s)]))
for x in sorted(ls): print(x)