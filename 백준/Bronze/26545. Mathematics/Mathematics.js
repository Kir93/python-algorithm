const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

console.log(
  input
    .slice(1)
    .map(Number)
    .reduce((acc, cur) => acc + cur, 0),
);
