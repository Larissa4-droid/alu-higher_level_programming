#!/usr/bin/node

const { argv } = require('node:process');

const arg1 = Number(argv[2]);
const arg2 = Number(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(arg1, arg2);
