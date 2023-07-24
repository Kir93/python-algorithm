ls = [input() for _ in range(int(input()))]
ils = sorted(ls)
dls = sorted(ls, reverse=True)
if ls == ils: print('INCREASING')
elif ls == dls: print('DECREASING')
else: print('NEITHER')