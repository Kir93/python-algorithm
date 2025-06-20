def solution(food):
    left = [str(i) * (food[i]//2) for i in range(1, len(food))]
    left_part = ''.join(left)
    return left_part + '0' + left_part[::-1]