function solution(n) {
  let answer = 0;

  for (let i = n; i > 0; i -= 2) {
    if (n % 2 === 0) {
      answer += i * i;
    } else {
      answer += i;
    }
  }

  return answer;
}