const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ');

const [N, M, K] = input.map(Number);
console.log(Math.min(M, K) + N - Math.max(M, K));