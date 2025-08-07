const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

let [a, b, c, d, e] = input.map(Number);
let ice = Boolean(a < 0);
let r = 0;

while (a !== b) {
  if (a < 0) {
    a += 1;
    r += c;
  } else if (a === 0 && ice) {
    r += d;
    ice = false;
  } else {
    a += 1;
    r += e;
  }
}

console.log(r);
