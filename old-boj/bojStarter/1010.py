import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)