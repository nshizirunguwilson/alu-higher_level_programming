#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (squareSize) {
  for (let i = 1; i <= squareSize; i++) {
    for (let j = 1; j <= squareSize; j++) {
      console.log('*');
    }
  }
} else {
  console.log('Missing size');
}
