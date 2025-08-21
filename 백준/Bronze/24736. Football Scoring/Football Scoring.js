const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [a, b] = input;
const [at, af, as, ap, ac] = a.split(' ').map(Number);
const [bt, bf, bs, bp, bc] = b.split(' ').map(Number);

console.log(
  `${at * 6 + af * 3 + as * 2 + ap + ac * 2} ${
    bt * 6 + bf * 3 + bs * 2 + bp + bc * 2
  }`,
);