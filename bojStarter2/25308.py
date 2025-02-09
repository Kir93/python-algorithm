from itertools import permutations as pm
import sys, math
input = sys.stdin.readline

num = list(map(int,input().split()))
arr = list(pm(num,8))

count = 0
for v in arr :
    x,y = [0]*10, [0]*10
    x[0],y[0] = v[0],0
    x[1],y[1] = v[1]/math.sqrt(2), v[1]/math.sqrt(2)
    x[2],y[2] = 0, v[2]
    x[3],y[3] = -v[3]/math.sqrt(2), v[3]/math.sqrt(2)
    x[4],y[4] = -v[4],0
    x[5],y[5] = -v[5]/math.sqrt(2), -v[5]/math.sqrt(2)
    x[6],y[6] = 0, -v[6]
    x[7],y[7] = v[7]/math.sqrt(2), -v[7]/math.sqrt(2)
    x[8],y[8] = v[0],0
    x[9],y[9] = v[1]/math.sqrt(2), v[1]/math.sqrt(2)

    valid = True
    for i in range(8) :
        fix = (x[i]*y[i+1] + x[i+1]*y[i+2] + x[i+2]*y[i]) - (x[i+1]*y[i] + x[i+2]*y[i+1] + x[i]*y[i+2])
        if fix <= 0 :
            valid = False

    if valid :
        count += 1
print(count)