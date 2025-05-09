import sys
input = sys.stdin.readline

def mutant(s, d):
    for i in range(len(s) + 1):
        for j in range(i, len(s) + 1):
            sub = s[:i] + s[i:j][::-1] + s[j:]
            d[sub] = True

for _ in range(int(input())):
    n, m = map(int, input().split())
    DNA = input().rstrip()
    marker = input().rstrip()

    d = dict()
    d[marker] = True
    mutant(marker, d)
    L = len(marker)

    res = 0
    for i in range(len(DNA)):
        tmp = DNA[i:i + L]
        if tmp in d.keys():
            res += 1

    print(res)