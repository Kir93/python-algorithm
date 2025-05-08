a = list(map(int, input().split()))
b = list(map(int, input().split()))

asum, bsum = 0, 0
cnt = 0

for i in range(9):
    asum += a[i]
    if asum > bsum and cnt == 0:
        cnt += 1
    if asum < bsum and cnt == 1:
        cnt += 1
    bsum += b[i]
    
if cnt == 2 and asum < bsum or cnt == 1 and asum < bsum: print("Yes")
else: print("No")