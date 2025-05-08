# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(4, n+1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                answer += 1
                break
    return answer

# retry
def solution(n):
    answer = 0
    for i in range(4, n+1):
        for j in range(2, int(i**0.5) + 1):
            if i%j == 0:
                answer += 1
                break
    return answer

# i를 0.5 제곱으로 하면 계산이 더 빨라짐.
# 왜냐하면 합성수란 3개의 약수를 가진다는 의미이고 1과 자기 자신은 이미 있기 때문에
# 1개의 약수만 찾으면 된다.