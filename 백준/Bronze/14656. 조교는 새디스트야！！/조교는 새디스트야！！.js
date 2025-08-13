const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const students = input[1].split(' ').map(Number);
console.log(students.filter((student, index) => student !== index + 1).length);