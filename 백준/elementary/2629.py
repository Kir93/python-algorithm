from sys import stdin
input = stdin.readline

n, w = int(input()), list(map(int, input().split()))
m, b = int(input()), list(map(int, input().split()))



dp = [[0 for _ in range((500 * j)+1)] for j in range(n+1)]
ans = []

def cal(num, weight): 
    if num > n: 
        return
    if dp[num][weight] == 1: 
        return
    dp[num][weight] = 1

    cal(num+1, weight + w[num-1])
    cal(num+1, weight)
    cal(num+1, abs(weight - w[num-1]))

cal(0, 0)

for bead in b:
    if bead > 500 * n:
        ans.append('N')
    elif dp[n][bead] == 1:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)