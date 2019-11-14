def heap_sort(a):
    size = len(a)
    for i in range(size, -1, -1):
      heap_heapify(a, size, i)
    for i in range(size-1, 0, -1):
      a[i], a[0] = a[0], a[i]
      heap_heapify(a, i, 0)
def heap_heapify(a, size, i):
    largest = i
    L = 2*i + 1
    R = 2*i + 2
    if L<size and a[i]<a[L]: largest = L
    if R<size and a[largest]<a[R]: largest = R
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heap_heapify(a, size, largest)
arr = [9,1,22,4,0,-1,1,22,100,10]
heap_sort(arr)
print( arr )
# [-1, 0, 1, 1, 4, 9, 10, 22, 22, 100]
