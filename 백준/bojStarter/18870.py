import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
arr = sorted(list(set(x)))
dic = {arr[i] : i for i in range(len(arr))}

for i in x: print(dic[i], end = ' ')