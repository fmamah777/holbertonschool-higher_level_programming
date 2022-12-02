#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
