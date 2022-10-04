# 자리수를 참고하여 문제를 해결하자
# 최대 자리수는 2자리까지
# 한 자리 씩 참고하자
# 결과 나누기 필수
# 첫글자 0, 중간 0에 대해 생각하자
ls = [0] + list(map(int, input()))
if ls[1] == 0: exit(print(0))
dp = [0] * len(ls)
dp[0] = dp[1] = 1
for i in range(2, len(ls)):
    if ls[i] != 0: dp[i] += dp[i-1]
    temp = ls[i-1] * 10 + ls[i]
    if temp >= 10 and temp <= 26: dp[i] += dp[i-2]
print(dp[-1]%1000000)