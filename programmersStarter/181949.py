# 대소문자 바꿔서 출력하기
str = input()
convertStr = ''
for s in str:
    if s.islower(): convertStr += s.upper()
    else: convertStr += s.lower()

print(convertStr)

# Best Solution
print(str.swapcase())