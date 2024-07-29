n = int(input())
array = list(map(int, input().split()))

result = [array[0]]
for i in range(1, n): result.append(array[i] * (i+1) - sum(result))
for i in result: print(i, end=' ')