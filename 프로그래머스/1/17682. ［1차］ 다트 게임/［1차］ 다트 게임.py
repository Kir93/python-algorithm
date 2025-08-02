import re

def solution(dartResult):
    rounds = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)

    scores = []

    for i, (score, bonus, option) in enumerate(rounds):
        score = int(score)
        if bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3

        if option == '*':
            score *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif option == '#':
            score *= -1

        scores.append(score)

    return sum(scores)