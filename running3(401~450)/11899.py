s = input()
while '()' in s:
    s = s.replace('()', '')
print(len(s))