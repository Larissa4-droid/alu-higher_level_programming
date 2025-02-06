#!/usr/bin/node

const { argv } = require('node:process');

const arg1 = Number(argv[2]);

if (!arg1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log('X'.repeat(arg1));
  }
}
