line = 0
result = 0
ls = list(input())
for i in range(1, len(ls)):
    if ls[i-1] == '(' and ls[i] == '(': line += 1
    elif ls[i-1] == '(' and ls[i] == ')': result += line
    elif ls[i-1] == ')' and ls[i] == ')':
        line -= 1
        result += 1
print(result)