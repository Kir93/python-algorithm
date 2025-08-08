function solution(n) {
  let answer = 0;

  for (let i = 1; i <= n ** 0.5; i++) {
    if (n % i === 0) {
      answer += 2;
    }
    if (i * i === n) {
      answer--;
    }
  }

  return answer;
}