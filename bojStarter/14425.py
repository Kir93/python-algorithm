import sys

N, M = map(int, sys.stdin.readline().split())
S = dict()
count = 0

for _ in range(N):
    word = sys.stdin.readline()
    S[word] = True

for _ in range(M):
    check = sys.stdin.readline()
    if check in S.keys():
        count+=1

print(count)