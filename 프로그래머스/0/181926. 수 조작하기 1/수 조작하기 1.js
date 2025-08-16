function solution(n, control) {
  for (c of control) {
    switch (true) {
      case c === 'w':
        n++;
        break;
      case c === 's':
        n--;
        break;
      case c === 'd':
        n += 10;
        break;
      case c === 'a':
        n -= 10;
        break;
    }
  }

  return n;
}