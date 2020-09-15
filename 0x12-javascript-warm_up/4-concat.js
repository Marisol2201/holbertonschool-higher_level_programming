#!/usr/bin/node
const args = process.argv;
if (args.length > 3) {
  console.log('c is cool');
} else if (args.length === 3) {
  console.log('c is undefined');
} else {
  console.log('undefined is undefined');
}
