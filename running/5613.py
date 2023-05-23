res = int(input())
while True:
    x = input()
    if x == '=': break
    n = int(input())
    if x == '+': res += n
    elif x == '-': res -= n
    elif x == '*': res *= n
    elif x == '/': res //= n
print(res)