import sys
#sys.stdin = open("input.txt", "r")


def DFS(x):
    if x == n+1:
        for i in range(x):
            if ck[i] == 1:
                print(i, end=" ")
        print()
    else:
        ck[x] = 1
        DFS(x+1)
        ck[x] = 0
        DFS(x+1)


if __name__ == "__main__":
    n = int(input())
    ck = [0 for i in range(n+1)]
    DFS(1)

#new code
import sys
sys.stdin = open("input.txt", "rt")


def DFS(n):
    if n > x:
        for s in r:
            print(s, end=' ')
        print()
        return
    else:
        r.append(n)
        DFS(n+1)
        print(r)
        r.pop()
        DFS(n+1)
        print(r)


if __name__ == "__main__":
    r = []
    x = int(input())
    DFS(1)

