function solution(arr, queries) {
  var answer = [];

  for ([s, e, k] of queries) {
    let temp = 100_000_000;
    for (let i = s; i <= e; i++) {
      if (arr[i] > k && arr[i] < temp) {
        temp = arr[i];
      }
    }
    answer.push(temp === 100_000_000 ? -1 : temp);
  }
  return answer;
}