import sys
sys.stdin=open("input.txt","rt")
data = [i for i in range(21)]
for _ in range(10):
  a, b = map(int,input().split())
  for i in range((b-a+1)//2):
    data[a+i], data[b-i] = data[b-i], data[a+i]

for i in range(1,21):
  print(data[i], end=' ')

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
cnt = [i for i in range(21)]
for i in range(10):
    ai, bi = map(int, input().split())
    l = bi-ai
    # print(l)
    for j in range(l//2+1):
        # print(cnt[ai+j], cnt[bi-j])
        cnt[ai+j], cnt[bi-j] = cnt[bi-j], cnt[ai+j]
    # print(cnt)
for x in range(1, len(cnt)):
    print(cnt[x], end=" ")
