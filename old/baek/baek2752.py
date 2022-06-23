data = list(map(int,input().split()))

for i in range(1,len(data)):
  while(i > 0 and data[i-1] > data[i]):
    data[i-1],data[i] = data[i], data[i-1]
    i -= 1

for i in data:
  print(i, end=' ')
