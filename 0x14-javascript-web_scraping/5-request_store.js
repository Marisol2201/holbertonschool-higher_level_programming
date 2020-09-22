#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
