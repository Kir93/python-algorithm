function solution(str_list) {
  let answer = [];
  for (let i = 0; i < str_list.length; i++) {
    if (str_list[i] === 'l') {
      answer = str_list.slice(0, i);
      break;
    }
    if (str_list[i] === 'r') {
      answer = str_list.slice(i + 1);
      break;
    }
  }
  return answer;
}