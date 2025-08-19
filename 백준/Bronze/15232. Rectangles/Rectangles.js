const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [r, c] = input.map(Number);

for (let i = 0; i < r; i++) {
  console.log('*'.repeat(c));
}