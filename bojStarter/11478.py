s=input()
total=set()

for i in range(len(s)):
    for j in range(i,len(s)): total.add(s[i:j+1])

print(len(total))