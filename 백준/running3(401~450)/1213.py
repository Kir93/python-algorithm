from collections import Counter
word = input()
check = Counter(word)
c = 0
r = ''
m = ''
for k, v in list(check.items()):
    if v%2 == 1:
        c += 1
        m = k
        if c >=  2:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check.items()):
    r += (k*(v//2))
print(r + m + r[::-1])