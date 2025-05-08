n = int(input())
mod = 1000000
f = [0, 1]
p = mod//10*15
for i in range(2, p): f.append((f[i-1] + f[i-2])%mod)
print(f[n%p])