# 홀수에서는 불가능하기 때문에 0
# 전꺼에 *3 + i-4(= dp[:i-2] > 홀수는 0이기 떄문에 한번에 sum) *2 + 2로 구할 수 있다.
# 그림을 그려보면 더 확실함