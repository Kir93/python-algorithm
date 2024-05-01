import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    phone_number = []
    for _ in range(n):
        phone_number.append(sys.stdin.readline().rstrip())
    
    phone_number.sort()

    answer = True
    for i in range(len(phone_number) - 1):
        if phone_number[i] == phone_number[i+1][:len(phone_number[i])]:
            answer = False
            break
    
    if answer:
        print("YES")
    else:
        print("NO")