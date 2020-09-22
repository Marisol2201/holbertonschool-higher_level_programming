#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    let movies = JSON.parse(body).results;
    for (let movie in movies) {
      let characters = movies[movie].characters;
      for (let charctr in characters) {
        if (characters[charctr].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
