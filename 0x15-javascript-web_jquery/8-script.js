#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  let movies = data.results;
  for (let i = 0; i < movies.length; i++) {
    $('ul#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
