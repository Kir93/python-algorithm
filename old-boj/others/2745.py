N, B = map(str, input().split())

# 방법 1
# print(int(N, int(B)))

# 방법 2
temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r = 0
for i in range(len(N)):
    r += temp.index(N[len(N)-i-1]) * (int(B)**i)
print(r)