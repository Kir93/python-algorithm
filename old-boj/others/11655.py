s = list(input())
c = []
for x in s:
    if x.isupper() and ord(x) <= 77: c.append(chr(ord(x)+13))
    elif x.isupper() and ord(x) > 77: c.append(chr(64+ord(x)+13-90))
    elif x.islower() and ord(x) <= 109: c.append(chr(ord(x)+13))
    elif x.islower() and ord(x) > 109: c.append(chr(96+ord(x)+13-122))
    else: c.append(x)
print("".join(c))