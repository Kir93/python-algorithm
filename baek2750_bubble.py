n = int(input())
data = []
for i in range(n):
  a = int(input())
  data.append(a)

for i in range(n):
  for j in range(1,n-i):
    if data[j-1] > data[j]:
      data[j-1], data[j] = data[j], data[j-1]

for i in data:
  print(i)
