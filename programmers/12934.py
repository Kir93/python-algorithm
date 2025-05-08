# 정수 제곱근 판별
def solution(n):
    x = int(n**0.5)
    return (x + 1) ** 2 if x * x == n else -1

# x = 121 ** 0.5  # 11.0으로 나와야 함
# print(x)  # 대부분 11.0이 나오지만, 간혹 10.999999999999998 이런 부동소수점 오차 발생 가능
# 그렇기 때문에 int()로 변환하여 정수로 바꾸고 x * x == n인지 확인하는게 더 좋음
# isqrt()를 사용하면 정수형으로만 계산하기 때문에 가장 성능도 좋고 정확함.

# Best Solution
from math import isqrt

def solution(n):
    x = isqrt(n)
    return (x + 1) ** 2 if x * x == n else -1