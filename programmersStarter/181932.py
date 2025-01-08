# 코드 처리하기
def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 if mode == 0 else 0
            continue
        if mode == 0 and i%2 == 0:
            ret += code[i]
        if mode == 1 and i%2 != 0:
            ret += code[i]
    
    return ret if ret != '' else 'EMPTY'