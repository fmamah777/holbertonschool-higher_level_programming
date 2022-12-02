#!/usr/bin/node
const args = process.argv;
const len = args.length;
let int;
let flag = 0;
if (len === 3) {
  int = parseInt(args[2]);
} else {
  flag = 1;
}
if (isNaN(int) || flag === 1) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < int; idx++) {
    console.log('C is fun');
  }
}
