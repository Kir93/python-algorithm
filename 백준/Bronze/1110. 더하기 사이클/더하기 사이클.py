n = input().zfill(2)
t = n
c = 0

while True:
    c += 1
    t = t[1] + str(int(t[0]) + int(t[1]))[-1]
    if n == t: break

print(c)