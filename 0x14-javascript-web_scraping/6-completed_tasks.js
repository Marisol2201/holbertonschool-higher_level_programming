#!/usr/bin/node
const request = require('request');
const taskcounter = {};
let user;

request(process.argv[2], function (err, request, body) {
  if (err) {
    console.log(err);
  }
  for (user of JSON.parse(body)) {
    if (user.completed === true) {
      if (taskcounter[user.userId] === undefined) {
        taskcounter[user.userId] = 0;
      }
      taskcounter[user.userId]++;
    }
  }
  console.log(taskcounter);
});
