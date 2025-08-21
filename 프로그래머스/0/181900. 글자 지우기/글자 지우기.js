function solution(my_string, indices) {
  return my_string
    .split('')
    .map((s, i) => (indices.includes(i) ? '' : s))
    .join('');
}