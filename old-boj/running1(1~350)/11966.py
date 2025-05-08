n = int(input())
s = [2**i for i in range(n if n < 31 else 31)]
print(1 if n in s else 0)