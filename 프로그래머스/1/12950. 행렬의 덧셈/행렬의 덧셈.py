import numpy

def solution(arr1, arr2):
    answer = numpy.array(arr1) + numpy.array(arr2)
    return answer.tolist()