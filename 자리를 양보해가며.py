page = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']

# 최종

sheet = [] * 3
second = 0
for x in page:
    if len(sheet) < 3:
        if x in sheet:
            sheet.append(sheet.pop(sheet.index(x)))
            second += 1
        else:
            sheet.append(x)
            second += 60
    else:
        if x in sheet:
            sheet.append(sheet.pop(sheet.index(x)))
            second += 1
        else:
            sheet.pop(0)
            sheet.append(x)
            second += 60

print(f'{second // 60}분 {second % 60}초')


#  첫 시도

chair = [[0, 0, 0] for _ in range(3)]
m = s = index = 0
for x in page:
    for i in range(3):
        if chair[i][0] == x:
            chair[i][1] += 1
            s += 1
            break
        elif chair[i][0] == 0:
            chair[i][0] = x
            m += 1
            for j in range(3):
                if chair[j][0] != x and chair[j][0] != 0:
                    chair[j][2] += 1
            break
    else:
        for j in range(3):
            if chair[j][0] != x and chair[j][0] != 0:
                chair[j][2] += 1
        rest = [99999, -99999]
        for i in range(3):
            if rest[0] > chair[i][1]:
                rest[0] = chair[i][1]
                rest[1] = chair[i][2]
                index = i
            elif rest[1] < chair[i][2]:
                rest[0] = chair[i][1]
                rest[1] = chair[i][2]
                index = i

        chair[index][0] = x
        chair[index][1] = 0
        chair[index][2] = 0
        m += 1

print(f'{m}분 {s}초')
