data = list(map(int, input().split()))

def quickSort(data):
  
  if len(data) <= 1: return data

  pivot = data[len(data)//2]
  left, equal, right = [],[],[]

  for i in data:
    if i < pivot:
      left.append(i)
    elif i == pivot:
      equal.append(i)
    else:
      right.append(i)
      
  return quickSort(left) + equal + quickSort(right)

data = quickSort(data)

for i in data:
  print(i,end=' ')
