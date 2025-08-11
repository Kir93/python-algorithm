function solution(hp) {
  let answer = 0;
  const damage = [5, 3, 1];

  for (const a of damage) {
    answer += Math.floor(hp / a);
    hp %= a;
  }

  return answer;
}