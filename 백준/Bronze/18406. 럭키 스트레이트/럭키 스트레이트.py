n = list(map(int, input()))
print("LUCKY" if sum(n[:len(n)//2]) == sum(n[len(n)//2:]) else "READY")