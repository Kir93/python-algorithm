import sys
input = sys.stdin.readline
endpoint = '!'

def dfs(cur_dict) :
  if not cur_dict :
    return 0
  next_list = list(cur_dict.keys())
  if len(next_list) == 1 :
    if cur_dict[next_list[0]][0] == 1 :
      return 0
    return dfs(cur_dict[next_list[0]][1])
  result = 0
  for next_w in next_list :
    result += cur_dict[next_w][0] + dfs(cur_dict[next_w][1])
  return result

def solve() :
  N = int(input())
  word_list = [input().strip() + endpoint for _ in range(N)]
  word_dict = dict()
  for word in word_list :
    cur_dict = word_dict
    for w in word :
      if w not in cur_dict :
        cur_dict[w] = [0, dict()]
      if w != endpoint :
        cur_dict[w][0] += 1
      cur_dict = cur_dict[w][1]

  result = 0
  for num, cur_dict in word_dict.values() :
    result += num + dfs(cur_dict)
  print('{:.02f}'.format(result / N))

try :
  while True:
    solve()
except :
  exit()