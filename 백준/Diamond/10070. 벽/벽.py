import sys
input = sys.stdin.readline

int1 = lambda: int(input().strip())
ints = lambda: list(map(int,input().split()))

N,K = ints()
arr = [0]*N
queries = [ints() for _ in range(K)]
INF = float('inf')

class SegTree:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr
        self.lazyl = [0 for _ in range(N<<2)]
        self.lazyr = [INF for _ in range(N<<2)]
        
    def update_lazy(self, idx, left, right):
        if left == right:
            v = self.arr[left]
            self.arr[left] = min(max(v, self.lazyl[idx]), self.lazyr[idx])
        else:
            for child in [idx<<1, (idx<<1)|1]:
                if self.lazyl[idx] <= self.lazyr[child]:
                    self.lazyl[child] = max(self.lazyl[child], self.lazyl[idx])
                else:
                    self.lazyl[child] = self.lazyl[idx]
                    self.lazyr[child] = self.lazyl[idx]
                if self.lazyr[idx] >= self.lazyl[child]:
                    self.lazyr[child] = min(self.lazyr[child], self.lazyr[idx])
                else:
                    self.lazyl[child] = self.lazyr[idx]
                    self.lazyr[child] = self.lazyr[idx]
                    
        self.lazyl[idx] = 0
        self.lazyr[idx] = INF
        
    def update_all(self, idx, left, right):
        self.update_lazy(idx, left, right)
        if left != right:
            m = (left+right) >> 1
            self.update_all(idx<<1, left, m)
            self.update_all((idx<<1)|1, m+1, right)
            
    def update_range(self, idx, left, right, i, j, v, op):
        self.update_lazy(idx, left, right)
        if j < left or right < i: return
        elif i <= left and right <= j:
            if op == 1: self.lazyl[idx] = v
            else: self.lazyr[idx] = v
        else:
            m = (left+right) >> 1
            self.update_range(idx<<1, left, m, i, j, v, op)
            self.update_range((idx<<1)|1, m+1, right, i, j, v, op)
            
seg = SegTree(N, arr)

for op,a,b,v in queries: seg.update_range(1,0,N-1,a,b,v,op)
seg.update_all(1,0,N-1)
for a in arr: print(a)