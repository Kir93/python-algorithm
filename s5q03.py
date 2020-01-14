import sys
#sys.stdin = open("input.txt", "r")


def DFS(x):
    if x == n+1:
        for i in range(x):
            if ck[i] == 1:
                print(i, end=" ")
        print()S
    else:
        ck[x] = 1
        DFS(x+1)
        ck[x] = 0
        DFS(x+1)


if __name__ == "__main__":
    n = int(input())
    ck = [0 for i in range(n+1)]
    DFS(1)
