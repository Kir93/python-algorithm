function solution(n, k) {
  let answer = [];
  for (let i = k; i <= n; i += k) {
    answer.push(i);
  }
  return answer;
}