function solution(num_list) {
  const filterFunc = (_, i) => i % 2 === 0;
  const sumFunc = (acc = 0, cur) => acc + cur;

  return Math.max(
    num_list.filter(filterFunc).reduce(sumFunc),
    num_list.slice(1).filter(filterFunc).reduce(sumFunc),
  );
}