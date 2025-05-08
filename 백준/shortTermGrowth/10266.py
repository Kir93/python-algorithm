import sys
input = sys.stdin.readline

def getPi(p):
    pi = [0] * len(p)
    j = 0
    
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]

        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def KMP(c1, c2):
    pi = getPi(c2)

    j = 0
    for i in range(0, len(c1)):
        while j > 0 and c1[i] != c2[j]:
            j = pi[j - 1]

        if c1[i] == c2[j]:
            if j == len(c2) - 1:
                return True
            else:
                j += 1
    return False

N = input()
clock1 = [0] * 360000
clock2 = [0] * 360000


for i in map(int, input().split()):
    clock1[i] = 1

clock1 += clock1

for i in map(int, input().split()):
    clock2[i] = 1

if KMP(clock1, clock2):
    print("possible")
else:
    print("impossible")