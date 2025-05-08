A, B, G = 0, 0, 0
Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']

n = int(input())
correct = input()

for i in range(n):
    if correct[i] == Adrian[i%3]: A += 1
    if correct[i] == Bruno[i%4]: B += 1
    if correct[i] == Goran[i%6]: G += 1
            
m = max(A, B, G)
print(m)

if m == A: print('Adrian')
if m == B: print('Bruno')
if m == G: print('Goran')