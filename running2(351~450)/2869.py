a, b, v = map(int, input().split())
r = (v-b)/(a-b)
print(int(r) if r == int(r) else int(r) + 1)