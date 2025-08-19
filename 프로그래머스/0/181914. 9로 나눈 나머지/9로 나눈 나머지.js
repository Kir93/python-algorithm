function solution(number) {
    return number.split('').reduce((acc, cur) => acc + parseInt(cur, 10), 0)%9;
}