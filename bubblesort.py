data = list(map(int,input().split()))

for i in range(len(data)):
  for j in range(len(data)-1):
    if data[i] < data[j]:
      data[i], data[j] = data[j], data[i]

for i in data:
  print(i, end=' ')
