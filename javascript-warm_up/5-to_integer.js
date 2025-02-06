#!/usr/bin/node

const { argv } = require('node:process');

const arg1 = Math.floor(Number(argv[2]));

if (arg1) {
  console.log('My number: ' + arg1);
} else {
  console.log('Not a number');
}
