import sys
input = sys.stdin.readline

def powmod(a,b,m):
    result = 1
    while b>0:
        if b%2 != 0:
            result = (result*a)%m
        b//=2
        a = (a*a)%m
    return result


def MillerRabin(n,a):
    r = 0
    d = n-1
    while(d%2==0):
        r += 1
        d //=2
    x = powmod(a,d,n)
    if x==1 or x==n-1:
        return True
    for i in range(0,r-1):
        x = powmod(x,2,n)
        if x==n-1:
            return True
    return False

if __name__=='__main__':
    ans = 0
    n = int(input())
    for _ in range(n):
        k = int(input())
        cnt = 0
        if k<4:
            ans+=1
            continue
        for i in [2,3,5,7,11]:
            if MillerRabin(2*k+1,i)==False:
                break
            else:
                cnt+= 1
        if cnt==5:
            ans+=1
    print(ans)