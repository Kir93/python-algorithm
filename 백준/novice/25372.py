for _ in range(int(input())):
    password = len(input())
    print("yes") if 6 <= password and password <= 9 else print("no")