def solve(l, s):
    if l == 0:
        visited.add(s)
        return
    for i in range(26):
        if alpha[i] >= 1:
            alpha[i] -= 1
            solve(l - 1, s + chr(i+97))
            alpha[i] += 1

for _ in range(int(input())):
    visited = set()
    alpha = [0 for _ in range(26)]
    string = input()

    for i in string: alpha[ord(i) - 97] += 1
    solve(len(string), '')
    for s in sorted(list(visited)): print(s)