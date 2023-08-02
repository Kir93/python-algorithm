n = int(input()[:-2]+'00')
f = int(input())
while n % f != 0: n += 1
print(str(n)[-2:])