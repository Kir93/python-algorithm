function solution(numbers) {
    const sortedNumbers = numbers.sort((a, b) => a - b)
    return sortedNumbers.at(-1) * sortedNumbers.at(-2);
}