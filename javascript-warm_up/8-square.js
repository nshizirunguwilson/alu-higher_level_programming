#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (squareSize) {
  for (let i = 1; i < squareSize; i++) {
    console.log('*'.repeat(squareSize));
  }
} else if (num < 0) {
  console.log();
} else {
  console.log('Missing size');
}
