# 종이 자르기
def solution(M, N):
    return (M - 1) + M * (N - 1)

# 최소값을 구하기 (가로, 세로 상관 없음)
# 가로로 자르는 경우 M - 1
# 세로로 자르는 경우 M * (N - 1)을 해주면 됨. (M개의 조각이 생겼기 때문에)

# retry
def solution(M, N):
    return (M - 1) + M * (N - 1)