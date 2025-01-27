#문자열 묶기
def solution(strArr):
    r = dict()
    for x in strArr:
        if len(x) not in r:
            r.setdefault(len(x), [x])
        else: r[len(x)] += [x]

    return max([len(x) for x in r.values()])

#Best solution
def solution(strArr):
    r = dict()
    for x in strArr:
        r[len(x)] = r.get(len(x), 0)
    return max(r.values())