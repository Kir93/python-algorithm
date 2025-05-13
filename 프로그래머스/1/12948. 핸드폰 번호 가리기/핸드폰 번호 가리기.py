def solution(phone_number):
    return f'{"*" * (len(phone_number) - 4)}{phone_number[-4:]}'