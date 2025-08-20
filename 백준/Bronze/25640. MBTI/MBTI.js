const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [target, _, ...mbti] = input;
console.log(mbti.filter((m) => m === target).length);