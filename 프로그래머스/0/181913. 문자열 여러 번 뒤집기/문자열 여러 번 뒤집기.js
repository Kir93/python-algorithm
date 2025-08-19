function solution(my_string, queries) {
  let list = my_string.split('');
  queries.forEach(([s, e]) => {
    list.splice(s, e - s + 1, ...list.slice(s, e + 1).reverse());
  });
  return list.join('');
}