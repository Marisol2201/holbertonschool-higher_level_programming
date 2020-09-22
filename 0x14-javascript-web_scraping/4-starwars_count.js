#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const movie in movies) {
      const characters = movies[movie].characters;
      for (const charctr in characters) {
        if (characters[charctr].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
