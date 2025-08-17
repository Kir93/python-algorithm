function solution(n) {
  var answer = [];
  while (n !== 1) {
    answer.push(n);
    if (n % 2 === 0) {
      n /= 2;
    } else {
      n = 3 * n + 1;
    }
  }
  return [...answer, 1];
}