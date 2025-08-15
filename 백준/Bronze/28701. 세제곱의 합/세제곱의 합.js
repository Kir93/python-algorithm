const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

n = parseInt(input[0], 10);
sumN = (n * (n + 1)) / 2;

console.log(sumN);
console.log(sumN ** 2);
console.log(sumN ** 2);