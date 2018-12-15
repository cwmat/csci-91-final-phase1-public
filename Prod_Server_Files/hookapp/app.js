var express = require('express');
var path = require('path');
var shell = require('shelljs');
var app = express();


app.locals.pending_process = false
app.locals.queue = false;


function run_script(){
  app.locals.pending_process = true

  shell.exec('/root/ProdContSetup.sh',{async:true},function(code, stdout, stderr){
    if (app.locals.queue == true){
      app.locals.queue = false;
      return run_script()
    }
    else{
      app.locals.pending_process = false;
      console.log ('All push requests have been executed');
    }
});
}


app.get('/payload', (req, res, next)=>{

  if (app.locals.pending_process == true){
    app.locals.queue = true;
  }
  else{
    run_script();
  }

  res.status(200).send('<p>The server is running</p>');
})

app.post('/payload', (req, res, next)=>{

  if (app.locals.pending_process == true){
    app.locals.queue = true;
  }
  else{
    run_script();
  }

  res.status(201).end();
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
