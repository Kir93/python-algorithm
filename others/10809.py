s = input()
a = [-1 for _ in range(26)]
for i in range(len(s)):
    if a[ord(s[i])-97] == -1:
        a[ord(s[i])-97] = i
for r in a: print(r, end=' ')