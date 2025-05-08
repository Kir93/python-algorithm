# 길이에 따른 연산
def multiply(arr):
    x = arr[0]
    for i in range(1, len(arr)):
        x *= arr[i]
        
    return x
        
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else multiply(num_list)

# Best solution 1
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

# Best solution 2
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)