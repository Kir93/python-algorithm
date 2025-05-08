import sys

def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
            
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

pat = sys.stdin.readline().rstrip()

ans = 0
for i in range(len(pat)):
    ans = max(ans, max(failure(pat[i:])))
    
print(ans)