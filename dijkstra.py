import queue

que = queue.Queue()
num = 6;
INF = 10000000;
d = [0 for i in range(num)]
v = [0 for i in range(num)]
a = [
  [0, 2, 5, 1, INF, INF],
	[2, 0, 3, 2, INF, INF],
	[5, 3, 0, 3, 1, 5],
	[1, 2, 3, 0, 1, INF],
	[INF, INF, 1, 1, 0, 2],
	[INF, INF, 5, INF, 2, 0]
]

def getSmallIndex():
  min = INF
  index = 0
  for i in range(num):
    if(d[i] < min and v[i]==0):
      min = d[i]
      index = i
  return index

def dijkstra(start):
  for i in range(num):
    d[i] = a[start][i]

  v[start] = 1

  for i in range(num-2):
    current = getSmallIndex()
    v[current] = 1
    for j in range(num):
      if v[j]==0:
        if d[current]+a[current][j] <d[j]:
          d[j] = d[current]+a[current][j]

if __name__ == "__main__":
  dijkstra(0)
  for i in range(num):
    print(d[i], end=" ")
