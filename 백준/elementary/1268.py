n = int(input())

students = [[0] * n for _ in range(n)]
datas = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(5):
        for k in range(n):
            if datas[i][j] == datas[k][j]:
                students[i][k] = 1

answers = [0] * n
for idx, s in enumerate(students):
    answers[idx] = s.count(1)

def printAnswer(answers):
    for i in range(n):
        if answers[i] == max(answers):
            print(i+1)
            return

printAnswer(answers)