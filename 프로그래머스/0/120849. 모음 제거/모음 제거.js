function solution(my_string) {
  removeString = ['a', 'e', 'i', 'o', 'u'];
  return my_string
    .split('')
    .filter((char) => !removeString.includes(char))
    .join('');
}