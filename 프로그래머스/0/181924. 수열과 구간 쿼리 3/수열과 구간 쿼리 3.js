function solution(arr, queries) {
  let answer = [...arr];
  queries.forEach(([i, j]) => {
    const temp = answer[i];
    answer[i] = answer[j];
    answer[j] = temp;
  });
  return answer;
}