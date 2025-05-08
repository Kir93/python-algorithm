ls = [int(input()) for _ in range(3)]
x = 'Error'
if ls.count(60) == 3: x = 'Equilateral'
elif sum(ls) == 180 and len(list(set(ls))) <= 2: x = 'Isosceles'
elif sum(ls) == 180 == 180: x = 'Scalene'
print(x)