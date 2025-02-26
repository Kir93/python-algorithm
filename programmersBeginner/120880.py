# 특이한 정렬
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))

# key로 정렬의 경우 괄호를 통해, 우선순위를 지정할 수 있다.
# -x로 내림차순 정렬을 하고, abs(x-n)으로 오름차순 정렬을 한다.