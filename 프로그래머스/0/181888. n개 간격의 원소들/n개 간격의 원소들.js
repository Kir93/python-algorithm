function solution(num_list, n) {
  return num_list.filter((_, i) => i % n === 0);
}