function solution(numbers, n) {
  return numbers.reduce((acc, cur) => {
    if (acc <= n) {
      acc += cur;
    }
    return acc;
  }, 0);
}