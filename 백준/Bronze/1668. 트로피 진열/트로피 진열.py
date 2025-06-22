ls = [int(input()) for _ in range(int(input()))]
left, right = 1, 1
left_part, right_part = ls[0], ls[-1]

for i in range(len(ls)):
    if ls[i] > left_part:
        left += 1
        left_part = ls[i]
    if ls[-i - 1] > right_part:
        right += 1
        right_part = ls[-i - 1]

print(left)
print(right)