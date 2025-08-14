function solution(ineq, eq, n, m) {
  let answer = true;

  switch (true) {
    case ineq === '>' && eq === '=':
      answer = Boolean(n >= m);
      break;
    case ineq === '<' && eq === '=':
      answer = Boolean(n <= m);
      break;
    case ineq === '>' && eq === '!':
      answer = Boolean(n > m);
      break;
    case ineq === '<' && eq === '!':
      answer = Boolean(n < m);
      break;
  }

  return answer ? 1 : 0;
}