import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

count = [0] * 1000001
stack = []
res = [-1] * n

for num in seq:
    count[num] += 1

for i in range(n):
    while stack and count[seq[stack[-1]]] < count[seq[i]]:
        res[stack.pop()] = seq[i]
    stack.append(i)

print(' '.join(map(str, res)))
