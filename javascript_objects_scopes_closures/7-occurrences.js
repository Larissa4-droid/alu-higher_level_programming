#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    const currentElement = list[i];
    if (currentElement === searchElement) {
      counter++;
    }
  }
  return counter;
};
