import sys

# dp : 2차원 배열로서 i번째 칸이 j번째 비트일 때 채울 수 있는 경우의 수
dp = [[-1] * (1 << 14) for _ in range(14 ** 2)]

# go : 가능한 모든 경우를 리턴하는 함수
def go(num, status):

    # Base Case 1 : 마지막 칸이 안 채워진 경우(=마지막 칸 - 1에서 옆으로 채운 경우)
    if num == n * m and status == 0:
        return 1
        
    # Base Case 2 : 마지막 칸을 넘어가는 경우
    if num >= n * m:
        return 0
        
    # Memoization
    if dp[num][status] != -1:
        return dp[num][status]
    dp[num][status] = 0
    
    # 현재 칸이 채워져있다면
    if status & 1:
        # 옆칸으로 이동
        dp[num][status] = go(num + 1, status >> 1)
        
    # 현재 칸이 안채워져있다면
    else:
        # 일단 밑에 칸을 채우고 옆칸으로 이동
        dp[num][status] = go(num + 1, status >> 1 | 1 << (m - 1))
        # 한 행의 마지막 칸이 아니라면 옆칸을 채우고 옆옆칸으로 이동
        if num % m != m - 1 and status & 2 == 0:
            dp[num][status] += go(num + 2, status >> 2)
    dp[num][status] %= 9901
    return dp[num][status]

# 입력부 및 정답 출력
n, m = map(int, sys.stdin.readline().split())
print(go(0, 0))