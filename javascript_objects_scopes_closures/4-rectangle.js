#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }
};
