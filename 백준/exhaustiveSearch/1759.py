vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
words = input().split()

words.sort() 

def check(arr):
    v_count, c_count = 0, 0

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def backtracking(arr):

    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < words[i]:
            arr.append(words[i])
            backtracking(arr)
            arr.pop()

for i in range(C - L + 1):
    a = [words[i]]
    backtracking(a)