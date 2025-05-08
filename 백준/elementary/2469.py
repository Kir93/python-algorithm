k = int(input())
n = int(input())
end = list(input())
start = sorted(end)
ladder = [list(input()) for _ in range(n)]
ladderS = []
ladderE = []

for i in range(len(ladder)):
  if ladder[i][0] == '?':
    ladderS = ladder[:i]
    ladderE = ladder[i+1:]
    break

for lad in ladderS:
  for i in range(k-1):
    if lad[i] == "-":
      start[i],start[i+1] = start[i+1],start[i]

ladderE.reverse()
for lad in ladderE:
  for i in range(k-1):
    if lad[i] == "-":
      end[i],end[i+1] = end[i+1],end[i]

answer = []
for i in range(len(start)-1):
  if start[i]==end[i]:
    answer.append("*")
  else:
    if start[i]==end[i+1]:
      answer.append("-")
    elif i!=0 and start[i]==end[i-1]:
      answer.append("*")
    else:
      answer = ['x' for _ in range(k-1)]
      break

print(''.join(answer))