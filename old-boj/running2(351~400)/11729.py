def hanoi(num, start, end):
    if num == 1: return print(start, end)
    hanoi(num - 1, start, 6 - start - end)
    print(start, end)
    hanoi(num - 1, 6 - start - end, end)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)