for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    print(f'Scenario #{i}:')
    print((n+m)*(m-n+1)//2, end='\n\n')