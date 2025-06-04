from sys import stdin
input = stdin.readline

for _ in range(3):
    s = 0
    for _ in range(int(input())):
        s += int(input())
    
    if s: print('+' if s > 0 else '-')
    else: print(s)