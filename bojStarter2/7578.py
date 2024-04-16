import sys
input = sys.stdin.readline

def locate(m, idx):
    acc_num = 0
    k = idx
    while k > 0:
        acc_num += fenwick_tree[k]
        k -= k & -k 

    k = idx
    while k <= n:
        fenwick_tree[k] += 1 
        k += k & -k 
    return m - acc_num
    
n = int(input())
fenwick_tree = [0]*(n+1)
loc = {}
count = 0
for i, a in enumerate(map(int, input().rstrip().split())):
    loc[a] = i+1
    
for i, b in enumerate(map(int, input().rstrip().split())):
    count += locate(i, loc[b])
    
print(count)