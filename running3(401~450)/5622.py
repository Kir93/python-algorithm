dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
r = 0
for i in range(len(a)):
    for x in dial:
        if a[i] in x:
            r += dial.index(x) + 3
print(r)