import sys; input = sys.stdin.readline

int(input())
a = set(map(int, input().split()))
int(input())
b = list(map(int, input().split()))
for x in b:
    if x in a: print(1)
    else: print(0)