import sys

word = sys.stdin.readline().rstrip()
N = len(word)
sa = [-1 for _ in range(N)] #sa[i] - i번째 suffix array 단어의 시작인덱스
pos = [0 for _ in range(N)] #pos[x] - 시작인덱스 x인 suffix의 그룹

def get_pos(x,d): #return pos[x+d]
    if x+d<N: return pos[x+d]
    else: return -1

def temp_same(x,y): #x,y d*=2 후의 그룹할당
    if pos[x]<pos[y]: return 1
    if pos[x]==pos[y]:
        if get_pos(x,d)<get_pos(y,d): return 1
    return 0

for i in range(N):
    sa[i] = i
    pos[i] = ord(word[i])-96


temp = [0 for _ in range(N)]
sa = sorted(sa, key=lambda x: (pos[x]))

d = 1
while True:
    sa = sorted(sa, key=lambda x: (pos[x], get_pos(x,d)))
    for i in range(N-1):
        temp[i+1] = temp[i] + temp_same(sa[i], sa[i+1])
    for i in range(N):
        pos[sa[i]] = temp[i]
    if temp[N-1]==N-1:
        break
    d*=2

order = [-1 for _ in range(N)]
for i in range(N):
    order[sa[i]] = i
lcp = [-1 for _ in range(N)]

d=0
for i in range(N):
    k = order[i]
    if k:
        j = sa[k-1]
        while j+d < N and i+d < N and word[j+d]==word[i+d]:
            d+=1
        lcp[k]=d
        if d:
            d -=1
    
for x in sa:
    print(x+1, end=' ')
print()
for x in lcp:
    if x == -1:
        print('x', end=' ')
    else:
        print(x, end=' ')