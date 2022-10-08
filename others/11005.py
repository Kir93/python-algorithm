# 진법 변환은 몫과 나누기라는 것을 인지하자
# 반복문 등호 말고 0이 아닐 때로
temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
r = ''
while n > 0:
    r += temp[n%b]
    n //= b
print(r[::-1])