#!/usr/bin/node
const prevSquare = require('./5-square');

/**
 * Class Sqaure inherits from rectangle
 */

class Square extends prevSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let row;
    for (let i = 0; i < this.height; i++) {
      row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
