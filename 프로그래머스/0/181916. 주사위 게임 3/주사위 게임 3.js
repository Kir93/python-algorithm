function solution(a, b, c, d) {
  var answer = 0;
  const numbers = [a, b, c, d];
  const counts = numbers.map((num) => numbers.filter((n) => n === num).length);

  if (Math.max(...counts) === 4) {
    answer = 1111 * a;
  } else if (Math.max(...counts) === 3) {
    const p = numbers.find((n) => numbers.filter((x) => x === n).length === 3);
    const q = numbers.find((n) => n !== p);
    answer = (10 * p + q) ** 2;
  } else if (Math.max(...counts) === 2) {
    if (Math.min(...counts) === 2) {
      const p = numbers.find(
        (n) => numbers.filter((x) => x === n).length === 2,
      );
      const q = numbers.find((n) => n !== p);
      answer = (p + q) * Math.abs(p - q);
    } else {
      answer = (a * b * c * d) / numbers[counts.indexOf(2)] ** 2;
    }
  } else {
    answer = Math.min(...numbers);
  }

  return answer;
}