import sys
# 힙 정렬
def heap_sort(data):
  size = len(data)
  for i in range(size, -1, -1):
    heap_heapify(data,size,i)
  for i in range(size-1,0,-1):
    data[i], data[0] = data[0], data[i]
    heap_heapify(data,i,0)
# 힙을 구성
def heap_heapify(data, size, i):
  large = i
  l = 2*i + 1
  r = 2*i + 2
  if l<size and data[i]<data[l]:  large = l
  if r<size and data[large]<data[r]:  large = r
  if large != i:
    data[i], data[large] = data[large], data[i]
    heap_heapify(data,size,large)
data = list(map(int,sys.stdin.readline().split()))
heap_sort(data)

for i in data:
  print(i,end=' ')
