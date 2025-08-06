const fs = require('fs');
const filePath = 'dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const GEC = {
  NLCS: 'North London Collegiate School',
  BHA: 'Branksome Hall Asia',
  KIS: 'Korea International School',
  SJA: 'St. Johnsbury Academy',
};

console.log(GEC[input])
