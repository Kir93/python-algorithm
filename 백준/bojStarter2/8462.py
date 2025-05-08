from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
queries = [[i] + list(map(lambda x : int(x)-1, input().split())) for i in range(M)]
queries.sort(key = lambda x : (x[1] // N ** 0.5, x[2]))

num_dict = defaultdict(int)
i, j, val = 0, -1, 0
ans = [0]*M

for idx, l, r in queries :
  while j < r :
    j += 1
    val += (2*num_dict[nums[j]] + 1)*nums[j]
    num_dict[nums[j]] += 1
  while j > r :
    val -= (2*num_dict[nums[j]] - 1)*nums[j]
    num_dict[nums[j]] -= 1
    j -= 1
  while i < l :
    val -= (2*num_dict[nums[i]] - 1)*nums[i]
    num_dict[nums[i]] -= 1
    i += 1
  while i > l :
    i -= 1
    val += (2*num_dict[nums[i]] + 1)*nums[i]
    num_dict[nums[i]] += 1
  ans[idx] = val

print(*ans, sep = '\n')