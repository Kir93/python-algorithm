# 가까운 1 찾기
def solution(arr, idx):
    try:
        return arr.index(1, idx)
    except ValueError:
        return -1

# 파이썬 try catch문은 try except로 사용