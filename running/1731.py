ls = [int(input()) for _ in range(int(input()))]
if ls[2] % ls[1] == 0: print(ls[-1] * (ls[2] // ls[1]))
else: print(ls[-1] + (ls[-1] - ls[-2]))