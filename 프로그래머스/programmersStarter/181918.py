# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        data = arr[i]
        if len(stk) == 0:
            stk.append(data)
            i += 1
        elif stk[-1] < data:
            stk.append(data)
            i += 1
        elif stk[-1] >= data:
            stk.pop()
    return stk

# Best solution
def solution(arr):
    stk = []
    for x in arr:
        while len(stk) and stk[-1] >= x: stk.pop()
        stk.append(x)
    return stk