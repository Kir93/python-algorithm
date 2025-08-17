const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ');

const [H, I, A, R, C] = input.map(Number);
console.log(H * I - A * R * C);
