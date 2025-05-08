num = 4;
INF = 10000000;
a = [
  [0, 5, INF, 8],
	[7, 0, 9, INF],
	[2, INF, 0, 4],
	[INF, INF, 3, 0]
]

def floydWarshall():
  d = [[0 for i in range(num)] for j in range(num)]
  for i in range(num):
    for j in range(num):
      d[i][j] = a[i][j]

# k = 거쳐가는 노드
  for k in range(num):
    # i = 출발 노드
    for i in range(num):
      # j = 도착 노드
      for j in range(num):
        if(d[i][k] + d[k][j] < d[i][j]):
          d[i][j] = d[i][k] + d[k][j]
  
  for i in range(num):
    for j in range(num):
      print("%3d" % d[i][j],end=' ')
    print()

if __name__ == "__main__":
  floydWarshall()
