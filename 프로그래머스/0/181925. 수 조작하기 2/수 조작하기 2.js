function solution(numLog) {
  const control = {
    1: 'w',
    '-1': 's',
    10: 'd',
    '-10': 'a',
  };
  let result = '';

  numLog.forEach((curr, index) => {
    if (index > 0) {
      const prev = numLog[index - 1];
      result += control[curr - prev] || '';
    }
  });

  return result;
}