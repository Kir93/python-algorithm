N = int(input())
list1 = list(map(int, input().split()))

list1.sort()

if N %2 ==0: print(list1[N//2 -1 ])
else: print(list1[N//2])