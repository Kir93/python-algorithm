for _ in range(3):
    ls = [int(input()) for _ in range(int(input()))]
    sum_ls = sum(ls)

    if sum_ls == 0: 
        print("0")
    elif sum_ls > 0:
        print("+")
    else:
        print("-")