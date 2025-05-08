data = list(map(int,input().split()))

for i in range(1,len(data)):
  while(i > 0 and data[i] < data[i-1]):
    data[i], data[i-1] = data[i-1], data[i]
    i -= 1

for i in data:
  print(i, end=' ')
