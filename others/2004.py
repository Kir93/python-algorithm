#펙토리얼 문제
# nCm = n!/m!*(n-m)! ex) 10C7 = 10!/7!*3! = 10*9*8/3*2*1 = n - (n-m) - m
# 0의 갯수 = 2*5의 갯수 구하면 됨
# 2개의 짝이 맞아야 되니까 2, 5중 작은 수가 0의 갯수
# 계산식은 min(countTwoFunc(n - (n-m) - m), countFiveFunc(n - (n-m) - m))
# count함수는 2, 5로 나눈 몫을 더하는 함수
