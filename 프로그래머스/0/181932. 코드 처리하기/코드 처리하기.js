function solution(code) {
  let mode = 0;
  var ret = '';

  for (i in code) {
    if (code[i] === '1') {
      mode = mode === 0 ? 1 : 0;
    } else {
      if (mode === 0 && i % 2 === 0) {
        ret += code[i];
      } else if (mode === 1 && i % 2 === 1) {
        ret += code[i];
      }
    }
  }

  return ret || 'EMPTY';
}