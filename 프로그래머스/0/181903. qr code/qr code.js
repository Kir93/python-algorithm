function solution(q, r, code) {
  return code
    .split('')
    .map((c, i) => (i % q === r ? c : ''))
    .join('');
}