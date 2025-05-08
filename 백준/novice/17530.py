values = []
for _ in range(int(input())):
    values.append(int(input()))
print('NS'[max(values)==values[0]])