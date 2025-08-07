function solution(dot) {
  const [x, y] = dot;

  switch (true) {
    case (x > 0) && (y > 0):
      return 1;
    case (x < 0) && (y > 0):
      return 2;
    case (x < 0) && (y < 0):
      return 3;
    default:
      return 4;
  }
}