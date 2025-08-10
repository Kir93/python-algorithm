const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

input.shift();
while (input.length) {
    const n = parseInt(input.shift(), 10);
    console.log(`${n} ${n}`);
}