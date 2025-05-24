import sys
from collections import deque
from array import array

input = sys.stdin.readline
n,k=map(int,input().split())

s = array('i',map(int,input().split()))

for i in range(1,n):
    s[i]+=s[i-1]
    
s.append(0)

bdp = array('q',[0]*n)
adp = array('q',[0]*n)

for i in range(1,n):
    bdp[i] = s[i-1]*(s[n-1]-s[i-1])

fr = tuple(array('i',[-1]*n) for _ in range(k))

def cross(f1,f2):
    a,b,t1 = f1
    c,d,t2= f2
    if c==a:
        return float('inf')
    return (b-d)//(c-a)

tk = k

for k in range(1,tk):
    j=k
    f=deque([(s[j-1],bdp[j]-s[n-1]*s[j-1],j)])
    st=deque([0])
    for i in range(k+1,n):
        find = s[i-1]
        while len(st)>=2 and st[1]<find:
            st.popleft()
            f.popleft()
        adp[i] = f[0][0]*s[i-1]+f[0][1]+s[i-1]*s[n-1]-s[i-1]**2
        fr[k][i] = f[0][2]
        nline = (s[i-1],bdp[i]-s[n-1]*s[i-1],i)
        while len(f)>1 and cross(nline,f[-1]) <= cross(f[-1],f[-2]):
            f.pop()
            st.pop()
        f.append(nline)
        st.append(cross(f[-1],f[-2]))
    adp,bdp = bdp,adp

res=0
ind=0

for i,v in enumerate(bdp):
    if res<=v:
        res = v
        ind = i

print(res)
back=[ind]
temp = ind

for i in range(tk-1,0,-1):
    back.append(fr[i][ind])
    ind = back[-1]
    
back.reverse()
print(*back)