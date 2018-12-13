var express = require('express');
var path = require('path');
var shell = require('shelljs');
var app = express();

app.set('views', path.join(__dirname,'views'));
app.set('view engine', 'pug');


app.get('/payload', (req, res, next)=>{
  //shell.exec('git clone git@github.com:scakaeze/webhook.git',{async:true})
  //shell.exec('/Users/Damien/Desktop/hookapp/test.sh')
  //console.log(app.get('views'))
  shell.exec('/root/ProdContSetup.sh',{async:true})
  res.status(200).send('<p>This is the local page</p>')
})

app.post('/payload', (req, res, next)=>{
  shell.exec('/root/ProdContSetup.sh',{async:true})
  res.status(201).end()
})




app.use(function (req, res, next) {
  res.status(404).send("Page cannot be found!")
});

app.use(function (err, req, res, next) {
  console.log('The Error Message: ' + err.message);
  //console.log('The Error Stack: ' + err.stack);
  res.status(500).send('There is an error with this request. Details: ' + err.message);
});


module.exports = app;
