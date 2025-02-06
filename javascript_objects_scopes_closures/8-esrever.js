#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  const arrLength = list.length;
  for (let i = arrLength - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return result;
};
