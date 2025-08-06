function solution(num_list) {
  let answer = [0, 0];
  num_list.forEach((num) => {
    if (num % 2 === 0) answer[0] += 1;
    else answer[1] += 1;
  });
  return answer;
}