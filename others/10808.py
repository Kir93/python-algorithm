s = input()
a = [0 for _ in range(26)]
for x in s: a[ord(x)-97] += 1
for r in a: print(r, end=' ')