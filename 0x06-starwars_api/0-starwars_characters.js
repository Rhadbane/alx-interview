#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function getCharacter (character) {
  return new Promise((resolve, reject) => {
    request(character, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function fetchCharacters (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const character of characters) {
      console.log(await getCharacter(character));
    }
  }
}

request(url, fetchCharacters);
