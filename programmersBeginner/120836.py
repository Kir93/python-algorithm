# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(n//i, 0, -1):
            if i * j == n:
                answer += 1
                break
    return answer

# Best solution
def solution(n):
    answer = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2
            if i * i == n:
                answer -= 1

    return answer

# retry
def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            answer += 2
        if i * i == n:
            answer -= 1
    return answer

# 순서 쌍의 경우 0.5제곱을 int로 줄인 뒤 + 1더해 순서대로 확인하며
# 약수일 경우 +2를 만약 앞과 뒤가 같은 경우 -1을 해주면 순서 쌍을 구할 수 있음.
# 예) 20 이라면 20의 0.5제곱을 int로 줄이면 4 + 1
# 20%1 = 0, 20%2 = 0, 20%4 = 0 3가지 순서 쌍이 있으니 2 * 3 = 6이 됨.
