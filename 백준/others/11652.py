# 마이너스가 올 수 있는 것을 생각하자
# sorted lambda를 이용하면 된다.
ls = {}
for _ in range(int(input())):
    x = int(input())
    if x in ls: ls[x] += 1
    else: ls[x] = 1
print(sorted(ls.items(), key=lambda x: (-x[1], x[0]))[0][0])