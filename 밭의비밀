#numpy 사용
import numpy as np
field1 = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
]

field2 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4],
    [0, 2, 0, 0, 2],
    [4, 5, 0, 2, 0],
]

rotfield = np.rot90(field2, 1)

sumfield = field1 + rotfield

for i in range(len(field1[0])):
    if i == 0:
        print(int(''.join([str(x) for x in sumfield[i]]), 8), end=' ')
    else:
        print(chr(int(''.join([str(x) for x in sumfield[i]]), 8)), end='')

#numpy 사용X
field1 = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
]

field2 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4],
    [0, 2, 0, 0, 2],
    [4, 5, 0, 2, 0],
]

newfield = [[0, 0, 0, 0, 0] for _ in range(5)]

for i in range(len(field2[0])):
    for j in range(len(field2[0])):
        newfield[i][j] = field2[j][-i-1]

for i in range(len(field2[0])):
    for j in range(len(field2[0])):
        newfield[i][j] += field1[i][j]

for i in range(len(newfield[0])):
    if i == 0:
        print(int(''.join(str(x) for x in newfield[i]), 8), end=' ')
    else:
        print(chr(int(''.join(str(x) for x in newfield[i]), 8)), end='')

