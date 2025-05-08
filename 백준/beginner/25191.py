c = int(input())
coke, beer = map(int, input().split())
e = coke//2 + beer

if c >= e: print(e)
else: print(c)