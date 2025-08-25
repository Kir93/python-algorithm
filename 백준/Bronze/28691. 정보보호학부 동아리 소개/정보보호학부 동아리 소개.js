const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'run/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const club = {
  M: 'MatKor',
  W: 'WiCys',
  C: 'CyKor',
  A: 'AlKor',
  $: '$clear',
};

console.log(club[input[0]]);