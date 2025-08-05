const fs = require('fs');
const filePath = 'dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

while (true) {
  const n = parseInt(input.shift());
  let r = 0;
  if (n === 0) break;
  console.log((n * (n + 1)) / 2);
}