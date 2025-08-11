const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let answer = '';
  for (const s of str) {
    if (s === s.toUpperCase()) {
      answer += s.toLowerCase();
    } else {
      answer += s.toUpperCase();
    }
  }
  console.log(answer);
});