#!/usr/bin/node
module.exports = class Rectangle {
  constructor (i, j) {
    if (i > 0 && j > 0) { [this.width, this.height] = [i, j]; }
  }

  print () {
    for (let o = 0; o < this.height; o++) console.log('X'.repeat(this.width));
  }
};
