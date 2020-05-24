stay = 1200202

stayDay = stay // 1200
monDay = [(2**i) for i in range(10, 0, -1)]
yearDay = sum(monDay)

year = stayDay // yearDay

divDay = stayDay % yearDay
sumMon = 0
month = 0
day = 0
divStay = 0
for i, x in enumerate(monDay):
    sumMon += x
    if i == 0 and divDay < sumMon:
        day = divDay
    if divDay < sumMon:
        month = i+1
        break
    else:
        day = divDay - x

lastStay = stay % 1200
hour = lastStay // 100 + 9

minStay = [25, 40, 55, 70, 85, 100]
minute = 0
divLastStay = (lastStay % 100) + 1
for i, x in enumerate(minStay):
    if divLastStay < x:
        minute = i * 10
        break

if divLastStay == 100:
    hour += 1
    minute = 0
    if hour == 21:
        hour = 9
        day += 1
        if day > monDay[month-1]:
            day = 1
            month += 1
            if month > 10:
                month = 1
                year += 1

print(f'{2020+year}년 {month}월 {day}일 {hour}시 {minute}분 출발')
