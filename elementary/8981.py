import sys

N = int(input())
result_list = list(map(int, input().split()))

answer_list = [0]*N

answer_list[0] = result_list[0]
idx = answer_list[0] % N

for value in result_list[1:] :
  while answer_list[idx] :
    idx = (idx + 1) % N

  answer_list[idx] = value
  idx = (idx + value) % N

print(N)
print(*answer_list)