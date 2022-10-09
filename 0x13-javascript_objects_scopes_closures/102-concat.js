#!/usr/bin/node
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const fs = require('fs');

let text = '';
if (file1 !== undefined && file2 !== undefined &&
    file3 !== undefined) {
  if ((fs.existsSync(file1) && fs.statSync(file1).isFile) &&
    (fs.existsSync(file2) && fs.statSync(file2).isFile)) {
    text += fs.readFileSync(file1, (error) => {
      if (error) throw error;
    });

    text += fs.readFileSync(file2, (error) => {
      if (error) throw error;
    });

    fs.writeFile(file3, text, (error) => {
      if (error) throw error;
    });
  }
}
