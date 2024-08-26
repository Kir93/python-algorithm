n = int(input())
max_list = []

for i in range(1, n + 1):
    my_list = [n]
    my_list.append(i)
    idx = 1

    while True:
        next_num = my_list[idx - 1] - my_list[idx]
        if next_num < 0: break
        my_list.append(next_num)
        idx += 1

    if len(max_list) < len(my_list): max_list = my_list

print(len(max_list))
for i in max_list: print(i, end=' ')