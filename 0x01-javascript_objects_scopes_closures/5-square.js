#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Class Sqaure inherits from rectangle
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
