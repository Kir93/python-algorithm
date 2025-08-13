int(input())
students = list(map(int, input().split()))
print(len([student for student, index in enumerate(students, start=1) if student != index]))