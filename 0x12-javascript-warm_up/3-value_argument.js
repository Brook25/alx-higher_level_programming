#!/usr/bin/node
// script prints the first argument passed to it
const arg = process.argv.slice(2);
if (!arg[0]) {
  console.log('No argument');
} else {
  console.log(arg[0]);
}
