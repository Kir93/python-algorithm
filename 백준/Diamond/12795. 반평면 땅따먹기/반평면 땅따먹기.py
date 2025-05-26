import sys 
input = sys.stdin.readline 

class Func: 
    def __init__(self, slope, intercept): 
        self.slope = slope  
        self.intercept = intercept 
    
    def get(self, x): 
        return (self.slope * x + self.intercept) 
    
class Node: 
    def __init__(self): 
        self.l = self.r = None 
        self.func = Func(0, float('-inf'))

class DST:
    def __init__(self): 
        self.root = Node()  

    def update(self, f): 
        s, e = -(10 ** 12), 10 ** 12 
        self.func(self.root, s, e, f) 
        return 
    
    def func(self, node, s, e,f): 
        high, low = f, node.func 
        if(high.get(s) < low.get(s)): 
            high, low = low, high 
        
        if(high.get(e) >= low.get(e)): 
            node.func = high 
            return

        middle = (s + e) // 2 
        if(high.get(middle) >= low.get(middle)):
            node.func = high 
            if(node.r is None): 
                node.r = Node()
            self.func(node.r, middle + 1, e, low)

        else: 
            node.func = low 
            if(node.l is None): 
                node.l = Node()
            self.func(node.l, s, middle, high) 

    def ans(self, x): 
        s, e = -(10 ** 12), 10 ** 12
        return self.query(self.root, s, e, x) 
    
    def query(self, node, s, e, x): 
        if(x < s or x > e or node is None): 
            return float('-inf') 
        
        v = node.func.get(x)
        
        middle = (s + e) // 2 
        if(x <= middle):
            return max(v, self.query(node.l, s, middle, x)) 
        else: 
            return max(v, self.query(node.r, middle + 1, e, x))
        

Q = int(input()) 
dst = DST() 

result = [] 
for _ in range(Q): 
    query = list(map(int, input().split(' ')[1 : ]))

    if(len(query) == 2):
        a, b = query 
        f = Func(a, b) 
        dst.update(f) 
    else:
        x = query[0] 
        result.append(str(dst.ans(x)))

print("\n".join(result)) 