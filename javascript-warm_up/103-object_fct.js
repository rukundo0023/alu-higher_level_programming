#!/usr/bin/node
let const = {
  type: 'object',
  value: 12
};
console.log(const);

const.incr = function () {
  this.value++;
};

const.incr();
console.log(const);
const.incr();
console.log(const);
const.incr();
console.log(const);
