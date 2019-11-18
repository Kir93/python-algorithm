import queue
import sys

que = queue.Queue()

for i in range(int(sys.stdin.readline())):
  que.put_nowait(sys.stdin.readline())
  print(que.get_nowait(i))
