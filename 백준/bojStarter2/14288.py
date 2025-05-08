import sys 
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline 

n, m = map(int, input().split()) 
parent = [0] + list(map(int, input().split()))

edge = [[] for _ in range(n + 1)] 
for i in range(2, n + 1, 1): 
    edge[parent[i]].append(i) 


idx = [-1 for _ in range(n + 1)] 
out = [-1 for _ in range(n + 1)] 
cnt = -1
def dfs(node):
    global cnt 

    cnt += 1 
    idx[node] = cnt 
    for nx in edge[node]: 
        dfs(nx) 
    
    out[node] = cnt 
    return 
dfs(1) 

h = 0 
while(2 ** h < n + 1): 
    h += 1 
cst = 2 ** h 
seg1 = [0 for _ in range(2 * cst)] 
seg2 = [0 for _ in range(2 * cst)] 

direct = 0
result = [] 
for _ in range(m): 
    com = list(map(int, input().split(' '))) 

    if(len(com) == 1):
        direct ^= 1 
    elif(len(com) == 2): 
        x = com[1]
        summation = 0 

        s, e = cst, idx[x] + cst 
        while(s <= e): 
            if(s % 2 == 1): 
                summation += seg1[s] 
            if(e % 2 == 0): 
                summation += seg1[e] 
            
            s = (s + 1) // 2 
            e = (e - 1) // 2 
        
        s, e = idx[x] + cst, out[x] + cst 
        while(s <= e): 
            if(s % 2 == 1): 
                summation += seg2[s] 
            if(e % 2 == 0): 
                summation += seg2[e] 
            
            s = (s + 1) // 2 
            e = (e - 1) // 2 

        result.append(str(summation))
    else: 
        x, w = com[1], com[2] 
        if(not direct): 
            i = idx[x] + cst 
            while(i): 
                seg1[i] += w 
                i = i // 2 

            i = out[x] + 1 + cst 
            while(i): 
                seg1[i] -= w 
                i = i // 2 
            
        else: 
            i = idx[x] + cst 
            while(i): 
                seg2[i] += w 
                i = i // 2 

print("\n".join(result)) 