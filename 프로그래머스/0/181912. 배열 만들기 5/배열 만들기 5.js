function solution(intStrs, k, s, l) {
  return intStrs
    .map((str) => parseInt(str.slice(s, s + l), 10))
    .filter((num) => num > k);
}