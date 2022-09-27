left = list(map(str, input()))
right = []
for _ in range(int(input())):
    x = list(map(str, input().split()))
    if x[0] == 'L' and left: right.append(left.pop())
    elif x[0] == 'D' and right: left.append(right.pop())
    elif x[0] == 'B' and left: left.pop()
    elif x[0] == 'P': left.append(x[1])
right.reverse()
left.extend(right)
print(''.join(left))