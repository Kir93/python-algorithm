buildings = []
for i in range(int(input())): buildings.append(int(input()))

stack = []
result = 0

for b in buildings:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)

  result += len(stack)-1

print(result)
