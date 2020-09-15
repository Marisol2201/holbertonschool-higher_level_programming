#!/usr/bin/node
const num = process.argv[2];
function factorial (n) {
  var total = 1;
  for (let i = 1; i <= n; i++) {
    total = total * i;
  }
  return total;
}
console.log(factorial(parseInt(num)));
