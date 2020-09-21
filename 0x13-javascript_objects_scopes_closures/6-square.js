#!/usr/bin/node
const Sqr = require('./5-square');
module.exports = class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) super.print();
    else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
