import sys

s = sys.stdin.readline().rstrip()
count = [[0] * 26]

q = int(sys.stdin.readline().rstrip())
for i, ch in enumerate(s):
    count.append(count[len(count) - 1][:])
    count[i + 1][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)