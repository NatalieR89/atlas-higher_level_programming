#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
        this.width = w;
        this.height = h;
      } else {
        // Return an empty object if conditions are not met
        return {};
      }
    }
  }
  
  module.exports = Rectangle;
  