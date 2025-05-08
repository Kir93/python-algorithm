import sys

def merge_sort(data):
  if len(data) > 1:

    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)

  else:
    return data

def merge(left, right):
  i=0
  j=0
  sort_data = []

  while (i<len(left)) & (j<len(right)):
    if left[i] < right[j]:
      sort_data.append(left[i])
      i+=1
    else:
      sort_data.append(right[j])
      j+=1
  
  while (i<len(left)):
    sort_data.append(left[i])
    i+=1
  while (j<len(right)):
    sort_data.append(right[j])
    j+=1
  return sort_data

data = list(map(int,sys.stdin.readline().split()))

for i in merge_sort(data):
  print(i,end=' ')
