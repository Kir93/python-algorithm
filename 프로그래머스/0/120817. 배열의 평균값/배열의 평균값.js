function solution(numbers) {
    return numbers.reduce((prev, b)=> prev + b, 0)/numbers.length;
}