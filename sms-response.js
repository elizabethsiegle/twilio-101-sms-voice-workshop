const http = require('http');
const express = require('express');
const { urlencoded } = require('body-parser');
const MessagingResponse = require('twilio').twiml.MessagingResponse;

const app = express();
app.use(urlencoded({ extended: false }));

app.post('/hack', (req, res) => {
  const twiml = new MessagingResponse();
  // Access the message body and the number it was sent from.
  const inbMsg = req.body.Body;
  if(inbMsg == "matcha") {
    twiml.message('The Robots are coming! Head for the hills!');
  }
  else {
      twiml.message("else");
  }
  res.writeHead(200, {'Content-Type': 'text/xml'});
  res.end(twiml.toString());
});

http.createServer(app).listen(1337, () => {
  console.log('Express server listening on port 1337');
});