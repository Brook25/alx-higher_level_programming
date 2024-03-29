#!/usr/bin/node
/* class Rectangle that defines a rectangle
The constructor takes 2 arguments w and h
Initializes the instance attribute width with the value of w
Initializes the instance attribute height with the value of h
If either of w or h is equal to 0 or not a positive integer, create an empty object */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
