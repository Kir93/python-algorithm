# 원소들의 곱과 합
from functools import reduce
def solution(num_list):
    return 1 if sum(num_list)**2 > reduce(lambda x, y: x * y, num_list) else 0

# Best solution
from math import prod
def solution(num_list):
    return 1 if sum(num_list)**2 > prod(num_list) else 0