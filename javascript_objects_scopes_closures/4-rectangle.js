#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
        this.width = w;
        this.height = h;
      } else {
        return {};
      }
    }
  
    // Print the rectangle using 'X'
    print() {
      if (this.width && this.height) {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      }
    }
  
    // Rotate the rectangle by swapping width and height
    rotate() {
      if (this.width && this.height) {
        [this.width, this.height] = [this.height, this.width];
      }
    }
  
    // Double the size of the rectangle
    double() {
      if (this.width && this.height) {
        this.width *= 2;
        this.height *= 2;
      }
    }
  }
  
  module.exports = Rectangle;
  