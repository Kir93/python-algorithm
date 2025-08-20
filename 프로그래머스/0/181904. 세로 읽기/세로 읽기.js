function solution(my_string, m, c) {
  let answer = '';
  let i = 0;

  my_string.split('').forEach((s) => {
    if (i == c - 1) {
      answer += s;
    }
    if (i == m - 1) {
      i = 0;
    } else {
      i++;
    }
  });

  return answer;
}