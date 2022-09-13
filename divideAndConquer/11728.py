from sys import stdin
input = stdin.readline
map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = a+b
r.sort()
print(*r)