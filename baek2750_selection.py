n = int(input())
data = []
for i in range(n):
  a = int(input())
  data.append(a)

for i in range(n):
  min = 9999
  for j in range(i,n):
    if min > data[j]:
      min = data[j]
      index = j

  data[i], data[index] = data[index], data[i]
  

for i in data:
  print(i)
