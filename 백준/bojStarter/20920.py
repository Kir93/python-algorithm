import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
word_lst = {}

for _ in range(N):
    word = input().rstrip()
    
    if len(word) < M: continue
    else:
        if word in word_lst: word_lst[word] += 1
        else: word_lst[word] = 1

word_lst = sorted(word_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_lst: print(i[0])