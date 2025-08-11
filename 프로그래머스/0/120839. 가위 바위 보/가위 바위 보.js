function solution(rsp) {
  const win = { 2: '0', 0: '5', 5: '2' };
  var answer = '';

  for (let i = 0; i < rsp.length; i++) {
    answer += win[Number(rsp[i])];
  }

  return answer;
}