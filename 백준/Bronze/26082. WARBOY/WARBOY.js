const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ');

const [a, b, c] = input;
console.log(((b/a) * 3) * c);