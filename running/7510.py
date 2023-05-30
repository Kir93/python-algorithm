for i in range(int(input())):
    ls = sorted(map(int, input().split()))
    print(f'Scenario #{i+1}:')
    print('yes\n' if ls[0]**2 + ls[1]**2 == ls[2]**2 else 'no\n')