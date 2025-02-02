import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def solution(A):
    if len(A) == 0:
        return

    tempL, tempR = [], []
    mid = A[0]
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
        tempL = A[1:]
    
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)