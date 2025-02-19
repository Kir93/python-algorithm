# 다항식 더하기
def solution(polynomial):
    xCount = 0
    nCount = 0
    for p in polynomial.split(' + '):
        print(p[:-1])
        if p.isdigit(): nCount += int(p)
        else: xCount += 1 if p == 'x' else int(p[:-1])

    if xCount == 0:
        return str(nCount)
    elif xCount == 1:
        return f'x + {nCount}' if nCount > 0 else 'x'
    else:
        return f'{xCount}x + {nCount}' if nCount > 0 else f'{xCount}x'