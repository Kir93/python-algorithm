ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input().rstrip()
for a in ca: x = x.replace(a, '!')
print(len(x))