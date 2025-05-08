N = int(input())

left_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))
result = 0

def make_dp():
  dp = [[-1]*(N+1) for _ in range(N+1)]
  dp[0][0] = 0

  for i in range(N):
    for j in range(N):
      if dp[i][j] > -1:
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if left_list[i] > right_list[j]:
          dp[i][j+1] = max(dp[i][j+1], dp[i][j] + right_list[j])
        
  return dp
  
def calculate(dp):
  max1 = max(dp[-1])
  max2 = max([ _dp[-1] for _dp in dp])

  return max(max1, max2)
  
if max(left_list) > max(right_list): print(sum(right_list))
else:
    dp = make_dp()
    result = calculate(dp)
    print(result)
