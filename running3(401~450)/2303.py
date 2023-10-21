s = []
n = int(input())
for _ in range(n):
    card = list(map(int, input().split()))
    maxD = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                d = (card[i] + card[j] + card[k]) % 10
                if d > maxD: maxD = d
    s.append(maxD)

for i in range(n-1, -1, -1):
    if s[i] == max(s):
        print(i+1)
        break