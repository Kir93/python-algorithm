function solution(my_string, queries) {
  let list = my_string.split('');
  for ([s, e] of queries) {
    list = list
      .slice(0, s)
      .concat(list.slice(s, e + 1).reverse(), list.slice(e + 1));
  }
  return list.join('');
}