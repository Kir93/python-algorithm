function solution(n) {
  return Array.from({ length: n + 1 }, (_, i) => {
    if (i % 2 === 0) return i;
    else return 0;
  }).reduce((prev, b) => prev + b, 0);
}