function solution(num_list) {
  return [
    ...num_list,
    num_list.at(-1) > num_list.at(-2)
      ? num_list.at(-1) - num_list.at(-2)
      : num_list.at(-1) * 2,
  ];
}