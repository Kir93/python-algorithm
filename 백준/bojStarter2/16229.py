import sys
input = sys.stdin.readline

n,k = map(int,input().split())
s = input().rstrip()

def z_array(s):
    n = len(s)
    l,r = 0,0
    z = [0]*n
    z[0] = n

    for i in range(1,n):
        if i > r:
            l,r = i,i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i-l
            if (z[k] < r-i+1):
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1

    return z

z = z_array(s)
ans = 0
for i in range(1,n):
    if z[i]+i == n and n+k >= ((n-1)//i+1)*i:
        ans = i
if k >= n:
    ans = n

print(ans)