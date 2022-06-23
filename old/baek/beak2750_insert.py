n = int(input())
data = []
for i in range(n):
  a = int(input())
  data.append(a)

for i in range(1,n):
  while(i > 0 and data[i-1] > data[i]):
    data[i], data[i-1] = data[i-1], data[i]
    i -= 1

for i in data:
  print(i)
