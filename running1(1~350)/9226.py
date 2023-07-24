m = ['a','e','i','o','u']
while True:
    s = list(input())
    if len(s) == 1 and s[0] == '#': break
    n = len(s)
    i = 0
    f = 0
    for x in s:
        if x in m:
            f = 1
            break
    if f==0:
        print(''.join(s)+'ay')
        continue
    else:
        while i <= n:
            if s[0] in m: break
            else:
                s.append(s.pop(0))
                i += 1
        print(''.join(s)+'ay')