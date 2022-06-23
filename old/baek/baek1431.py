import sys
def isNumber(s) :
    try:
        float(s)
        return True
    except ValueError:
        return False

n = int(sys.stdin.readline())
voca_list = []
for i in range(n) :
    a = sys.stdin.readline().strip()
    c = 0
    for j in a :
        if isNumber(j) :
            c = c + int(j)
    voca_list.append((len(a), c, a))
#sort
voca_list.sort() # sort() 함수 사용 시 가장 뒤에 있는 원소들부터 정렬해간다
for len_voca,num, voca in voca_list:
    print(voca)
