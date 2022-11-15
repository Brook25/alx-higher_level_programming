#!/usr/bin/node
/*  script prints the title of a Star Wars movie where the episode number
matches a given integer.
The first argument is the movie ID
https://swapi-api.hbtn.io/api/films/:id */

const arg = process.argv;
const movieId = arg[2];
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const req = require('request');
req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
