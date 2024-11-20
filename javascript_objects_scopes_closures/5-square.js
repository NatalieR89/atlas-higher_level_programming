#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    // Call the parent class's constructor with size as both width and height
    super(size, size);
  }
}

module.exports = Square;
