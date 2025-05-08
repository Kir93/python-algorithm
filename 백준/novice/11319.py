vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    s = input()
    c = v = 0
    for t in s:
        if t in vowels:
            v += 1
        elif t.isalpha():
             c += 1
    print(c, v)