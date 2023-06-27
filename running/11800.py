d = ['','Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
de = ['', 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy','Dabash', 'Dosh']
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b: print(f'Case {i+1}: {de[a]}')
    elif (a == 6 and b == 5) or (a == 5 and b == 6): print(f'Case {i+1}: Sheesh Beesh')
    else: print(f'Case {i+1}: {d[max(a, b)]} {d[min(a, b)]}')
