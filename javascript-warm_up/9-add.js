#!/usr/bin/node

const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
  return a + b;
}

const sum = add(num1, num2);

console.log(sum);
