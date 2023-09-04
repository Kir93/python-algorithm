from math import gcd
ca, cb = map(int, input().split())
ma, mb = map(int, input().split())
n = gcd((ca*mb + ma*cb), cb*mb)
print((ca*mb + ma*cb)//n, cb*mb//n)