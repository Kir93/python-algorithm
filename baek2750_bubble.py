n = int(input())
data = []
for i in range(n):
  a = int(input())
  data.append(a)

for i in range(n):
  for j in range(n):
    if data[i] < data[j]:
      data[i], data[j] = data[j], data[i]

for i in data:
  print(i)
