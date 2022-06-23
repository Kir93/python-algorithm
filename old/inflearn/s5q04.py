#bestcode
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")
    
#mycode
import sys
#sys.stdin = open("input.txt", "rt")
def DFS(n):
    m = "NO"
    ct = t.copy()
    if n > x-1:
        ct = list(set(ct) - set(r))
        if sum(r) == sum(ct):
            print("YES")
            sys.exit()
    else:
        r.append(ct.pop(n))
        DFS(n+1)
        r.pop()
        DFS(n+1)
if __name__ == "__main__":
    x = int(input())
    t = list(map(int, input().split()))
    r = []
    DFS(1)
    print("NO")
