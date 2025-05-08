S = list(input())
K = input()
new = []

for s in S:
    if ord(s) >= 65 and ord(s) < 91: new.append(s)
    elif ord(s) >= 97 and ord(s) < 123: new.append(s)
new = ''.join(new)

print(1) if K in new else print(0)