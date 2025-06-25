n, l = map(int, input().split())
last_num = 0
i = 0

while n > 0:
    i += 1
    if str(l) not in str(i):
        last_num = i
        n -= 1
    
print(last_num)