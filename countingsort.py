import random

count = [0 for i in range(6)]
data = [random.randint(1,5) for i in range(30)]

for i in range(1,30):
  count[data[i]]+=1
for i in range(1,6):
  if count[i] != 0:
    for j in range(count[i]):
      print(i,end=' ')
