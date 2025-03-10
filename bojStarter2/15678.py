from collections import deque

n, d = map(int, input().split())
dp = [0]
dp.extend(map(int, input().split()))
deq = deque()
for i in range(1, n+1):
    while deq:
    	# i-d 보다 왼쪽의 값은 삭제
        if deq[0][0] < i-d:
            deq.popleft() 
        else:
        	# 최댓값은 첫번째 값
            dp[i] = max(dp[i], dp[i]+deq[0][1])
            break
    while deq:
    	# 뒤에서부터 현재 값보다 작은 값은 모두 삭제
        if deq[-1][1] < dp[i]:
            deq.pop()
        else:
            break
    deq.append((i, dp[i]))
print(max(dp[1:]))