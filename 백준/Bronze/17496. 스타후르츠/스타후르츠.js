const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ');

const [n, t, c, p] = input.map(Number);
console.log(c * p * Math.floor((n - 1) / t));
