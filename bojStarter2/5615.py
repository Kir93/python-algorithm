def powmod(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

def mr(n,a):
    r = 0
    d = n-1
    while (d%2 == 0):
        r += 1
        d = d // 2
    x = powmod(a,d,n)
    if x == 1 or x == n-1:
        return True
    for i in range(0,r-1):
        x = powmod(x,2,n)
        if x == n-1:
            return True
    return False

import sys
ans = 0
m = int(sys.stdin.readline())
for i in range(m):
    k = int(sys.stdin.readline())
    check = 0
    for i in [2, 3,5,7,11]:
        if mr(2*k+1,i) == False:
            break
        else:
            check += 1
    if check == 5:
        ans += 1
print(ans)