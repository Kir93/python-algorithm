function solution(n) {
    return [...String(n)].map(Number).reduce((acc, cur) => acc + cur, 0);
}