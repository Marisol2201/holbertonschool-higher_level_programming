#!/usr/bin/node
const args = process.argv;
const string1 = 'c'
const string2 = 'is'
const string3 = 'cool'
const string4 = 'undefined'
if (args.length > 3) {
  console.log(string1 + ' ' + string2 + ' ' + string3);
} else if (args.length === 3) {
  console.log(string1 + ' ' + string2 + ' ' + string4);
} else {
  console.log(string4 + ' ' + string2 + ' ' + string4);
}
