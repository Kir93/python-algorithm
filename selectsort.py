data = list(map(int,input().split()))

for i in range(len(data)):
  min = 9999
  for j in range(i+1,len(data)):
    if min > data[j]:
      min = data[j]
      index = j

  data[i], data[index] = data[index], data[i]

for i in data:
  print(i, end=' ')
