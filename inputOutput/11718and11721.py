# 11718, 11719
while True:
    try:
        print(input())
    except:
        break

# 11720
n = int(input())

# import sys
# print(sum(map(int, sys.stdin.read(n)))) // n 정확하게 사용
print(sum(map(int, input())))

# 11721
word = input()

for i in range(0,len(word),10):
    print(word[i:i+10])