import math

def findCase(n): # n의 모든 약수를 찾아 내림차순으로 정렬 후 반환
    result = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if(i != n//i):
                result.append(n//i)

    result.sort(reverse=True)  # 내림차순으로 정렬
    return result

answer = []
while True:
    command = input()
    if command == ".":
        break

    commandLen = len(command)
    commandCase = findCase(commandLen)  # 입력받은 문자열의 약수들을 담음

    n = 0
    for e in commandCase:
        if command == (command[:commandLen//e]*e):
            n = e
            break
    answer.append(n)

for e in answer:
    print(e)