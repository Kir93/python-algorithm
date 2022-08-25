# 유클리드 호제법으로 다시 풀기

x, y = map(int, input().split())
big = 0
small = max(x,y)
xc = yc = 1
if x>y: flag = x
else: flag = y
for i in range(1, max(x+1, y+1)):
    if x%i == 0 and y%i == 0: big = i
while True:
    if flag == x:
        cf = y
        cc = yc
    else:
        cf = x
        cc = xc
    if small == cf*cc:
        break
    elif small < cf*cc:
        small = cf*cc
        if cf == x: flag = x
        else: flag = y
    if cf == x: xc += 1
    else: yc += 1
print(big)
print(small)