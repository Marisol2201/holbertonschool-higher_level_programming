#!/usr/bin/node
const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(num); i++) {
    console.log('X'.repeat(parseInt(num)));
  }
}
