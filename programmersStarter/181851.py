# 전국 대회 선발 고사
def solution(rank, attendance):
    answer = {}
    for i, b in enumerate(attendance):
        if b: answer[rank[i]] = i
        
    l = sorted(answer.keys())
    
    return (10000 * answer[l[0]]) + (100 * answer[l[1]]) + answer[l[2]]

# Best solution
def solution(rank, attendance):
    a, b, c = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])[:3]
    return 10000 * a[1] + 100 * b[1] + c[1]