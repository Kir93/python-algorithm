data = list(map(int,input().split()))

for i in range(len(data)):
  for j in range(1,len(data)-i):
    if data[j-1] > data[j]:
      data[j-1], data[j] = data[j], data[j-1]

for i in data:
  print(i, end=' ')
