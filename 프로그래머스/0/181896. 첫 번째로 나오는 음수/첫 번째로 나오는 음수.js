function solution(num_list) {
  return num_list.indexOf(num_list.filter((v) => v < 0)[0]) ?? -1;
}