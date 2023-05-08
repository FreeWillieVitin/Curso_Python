const fs = require('fs');
const path = require('path')
require('cross-fetch/polyfill');

pessoas = [
    {
        nome: 'Victor',
        sobrenome: 'Hugo',
        idade: 25,
        ativo: false,
        notas: ['A','A+'],
        telefones:{
            residencial: '47 3642-2414',
            celular: '47 99292-6812',
        }
    },
    {
        nome: 'Luiz',
        sobrenome: 'Carlos',
        idade: 51,
        ativo: true,
        notas: ['B','A'],
        telefones:{
            residencial: '47 3642-2414',
            celular: '47 98402-7387',
        },
    },
];

const saveTo = path.resolve(__dirname, 'arquivo-javascript.json');

fetch('https://jsonplaceholder.typicode.com/posts')
  .then(Response => Response.json())
  .then(json => {
    console.log(json)
    fs.writeFileSync(saveTo, JSON.stringify(json, null, 2));
  })

const json = require('./arquivo-javascript.json')
json.forEach(post => console.log(post.title))