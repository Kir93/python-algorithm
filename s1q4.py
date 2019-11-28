import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int,input().split()))
avg = round(sum(data)/n)
MIN = 99999
for idx, i in enumerate(data):
    temp = abs(avg-i)
    if temp < MIN:
        MIN = temp
        num = idx+1
    elif temp == MIN:
        if i > data[num-1]:
            num = idx +1
print(avg, num)

