n, m = map(int, input().split())

result = 0
if n == 1: result = 1
elif n == 2: 
  if m >= 1 and m <= 6: result = (m + 1) // 2 
  elif m >= 7: result = 4
elif n >= 3: 
  if m <= 6: result = min(m, 4)
  elif m >= 7: result = m - 2
  
print(result)