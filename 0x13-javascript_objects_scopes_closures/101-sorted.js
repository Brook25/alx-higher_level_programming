#!/usr/bin/node
const dict = require('./101-data').dict;
const n_wDict = {};
for (const key in dict) {
  if (n_wDict[dict[key]]) {
    n_wDict[dict[key]].push(key);
  } else {
    n_wDict[dict[key]] = [key];
  }
}
console.log(n_wDict);
