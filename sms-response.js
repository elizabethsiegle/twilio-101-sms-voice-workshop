const http = require('http');
const express = require('express');
const MessagingResponse = require('twilio').twiml.MessagingResponse;

const app = express();
app.use(express.urlencoded({ extended: false }));
app.post('/femmehacks', (req, res) => {
  const twiml = new MessagingResponse();
  // Access the message body and the number it was sent from.
  const inbMsg = req.body.Body.toLowerCase().trim();
  if(inbMsg == "thai tea") {
    twiml.message('That is my favorite boba flavor as well!');
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

