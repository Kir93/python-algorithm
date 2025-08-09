function solution(my_string, n) {
  return my_string
    .split('')
    .map((char) => char.repeat(n))
    .join('');
}