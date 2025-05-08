n = input()
isOk = False
for i in range(1, len(n)):
    s1, s2 = n[:i], n[i:]
    m1 = m2 = 1
    for i in s1: m1 *= int(i) 
    for i in s2: m2 *= int(i)
    if m1 == m2:
        isOk = True
        break
print('YES' if isOk else 'NO')