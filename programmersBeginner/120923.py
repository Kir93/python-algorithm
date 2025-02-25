# 연속된 수의 합 - retry
def solution(num, total):
    start = (total - (num * (num - 1) // 2)) // num
    return [start + i for i in range(num)]

# 등차수열을 통해 구하는 문제
# 1부터 n까지의 합은 n(n+1) // 2이다.
# num=5라면 n부터 5까지의 합은 n, n+1, n+2, n+3, n+4로 5n + 10이다.
# 5n + 10의 10 부분은 등차수열 공식에서 1부터 4까지의 합 4(4+1) // 2 = 10이다.
# 따라서 n부터 num까지의 합은 num * n + ((num - 1) * num // 2) = total로 표현할 수 있다.
# n을 구하기 위해서는 num * n = total - ((num - 1) * num // 2)
# n = (total - ((num - 1) * num // 2)) // num