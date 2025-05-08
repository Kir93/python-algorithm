n = int(input())
while True:
    flag = True
    for x in str(n):
        if x != '4' and x != '7':
            flag = False
            n -= 1
            break
    if flag:
        print(n)
        break