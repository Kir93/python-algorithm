MAX = float('inf')

def simplify(lst) :
  result = [lst[0]]
  for num in lst :
    if result[-1] != num :
      result.append(num)

  return result

_, _ = map(int, input().split())
bulb_list = list(map(int, input().split()))
bulb_list = simplify(bulb_list)

N = len(bulb_list)

dp = [[MAX]*N for _ in range(N)]

for i in range(N) :
  dp[i][i] = 0
  if i == N-1 :
    break
  dp[i][i+1] = 1

for i in range(2, N) :
  for j in range(N-i) :
    bulb_diff = 0 if bulb_list[j] == bulb_list[j+i] else 1
    for k in range(j, j+i) :
      dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + bulb_diff)

print(dp[0][-1])