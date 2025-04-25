number = int(input())

answer = 0

# for i in range(1): --> default 이렇게 하면 한번만 반복됨
while number:
    answer += number % 100
    number //= 100

print(answer)