function solution(my_string) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const alphabetList = alphabet.toUpperCase() + alphabet;
  return alphabetList
    .split('')
    .map((c) => my_string.split('').filter((x) => x === c).length);
}