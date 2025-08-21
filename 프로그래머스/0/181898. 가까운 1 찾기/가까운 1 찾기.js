function solution(arr, idx) {
  return arr.slice(idx).findIndex((v) => v === 1) >= 0
    ? idx + arr.slice(idx).findIndex((v) => v === 1)
    : -1;
}