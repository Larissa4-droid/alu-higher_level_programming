#!/usr/bin/node

const { argv } = require('node:process');

const numbers = argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  const uniqueSortedNumbers = numbers.sort((a, b) => b - a);
  console.log(uniqueSortedNumbers[1]);
}
