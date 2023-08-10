n = int(input())
r = 0
for i in range(1, n):
    if i**2 - (i-1)**2 > n: break
    for j in range(1, i+1):
        if i**2 - j**2 == n: r += 1
print(r)