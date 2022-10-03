#!/usr/bin/node
// script prints two arguments passed to it, in the following format: “is”
const args = process.argv.slice(2);
if (!args[0]) {
  console.log(args[0] + ' is ' + args[1]);
} else if (args.length === 1) {
  console.log(args[0] + ' is ' + args[1]);
} else {
  console.log(args[0] + ' is ' + args[1]);
}
