from math import factorial

def solve(s, i):
    global cnt
    if i == len(ls):
        cnt += 1
        if cnt == numN:
            return s
    else:
        for w in ls:
            if w not in s:
                r = solve(s + w, i + 1)
                if r: return r

while True:
    try:
        cnt = 0
        ls, n = map(str, input().split())
        numN = int(n)
        many = factorial(len(ls))
        if numN > many: 
            print(f'{ls} {n} = No permutation')
            continue
        print(f'{ls} {n} = {solve("", 0)}')

    except EOFError:
        break