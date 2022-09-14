n = int(input())
r = 1
c = 0
for i in range(1, n+1):
    r*=i
for x in reversed(str(r)):
    if x == '0': c += 1
    else: break
print(c)