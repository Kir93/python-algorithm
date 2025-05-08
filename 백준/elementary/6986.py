import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = []
for _ in range(N):
    a = float(input())
    scores.append(a)
scores.sort()
if K == 0:
    print('{:.2f}'.format(sum(scores)/len(scores)))
    print('{:.2f}'.format(sum(scores) / len(scores)))
else:
    cut = scores[K:-K]
    corrected = scores.copy()
    for i in range(K):
        corrected[i], corrected[-i-1] = corrected[K], corrected[-K-1]
    print('{:.2f}'.format(sum(cut)/len(cut)+ 0.00000001))
    print('{:.2f}'.format(sum(corrected)/len(corrected)+ 0.00000001))